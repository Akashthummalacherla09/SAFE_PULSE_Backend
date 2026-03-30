from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer, ProfileSerializer
from .models import Profile

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class CheckEmailView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    @method_decorator(csrf_exempt)
    def post(self, request):
        email = request.data.get('email')
        exists = User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists()
        return Response({'exists': exists, 'email': email})

class PasswordResetView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    @method_decorator(csrf_exempt)
    def post(self, request):
        email = request.data.get('email')
        new_password = request.data.get('password')
        
        user = User.objects.filter(email=email).first() or User.objects.filter(username=email).first()
        if user:
            user.set_password(new_password)
            user.save()
            return Response({'success': True})
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # AUTO-PROVISION DEFAULT ADMIN FOR INITIAL SETUP
        is_admin_attempt = (username.lower() in ['admin', 'admin@safepulse.com']) and (password == 'admin12')
        
        if is_admin_attempt:
            admin_user, created = User.objects.get_or_create(
                username='admin@safepulse.com', 
                defaults={'email': 'admin@safepulse.com', 'is_staff': True}
            )
            # Ensure the password and profile are correct even if account already existed
            admin_user.set_password('admin12')
            admin_user.is_staff = True
            admin_user.save()
            from .models import Profile
            Profile.objects.update_or_create(user=admin_user, defaults={'role': 'admin', 'full_name': 'SafePulse Admin System'})
            # Ensure we authenticate with the correct canonical username
            username = 'admin@safepulse.com'
        
        user = authenticate(username=username, password=password)
        if user:
            # Force admin12 as the actual token key for the admin user
            if user.username == 'admin@safepulse.com':
                token = Token.objects.filter(user=user).first()
                if not token:
                    token = Token.objects.create(user=user, key='admin12')
                elif token.key != 'admin12':
                    token.delete()
                    token = Token.objects.create(user=user, key='admin12')
            else:
                token, created = Token.objects.get_or_create(user=user)
                
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'name': user.profile.full_name if hasattr(user, 'profile') else user.username,
                'role': user.profile.role if hasattr(user, 'profile') else 'user'
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
