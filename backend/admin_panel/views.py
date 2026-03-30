from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
from assessments.models import HealthAssessment
from assessments.serializers import HealthAssessmentSerializer
from django.db.models import Count, Max

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or (hasattr(request.user, 'profile') and request.user.profile.role == 'admin'))

class UserManagementView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    
    def get(self, request):
        users = User.objects.select_related('profile').annotate(
            report_count=Count('assessments'),
            last_report=Max('assessments__timestamp')
        ).order_by('-id').all()
        
        data = []
        for u in users:
            profile = getattr(u, 'profile', None)
            data.append({
                'id': u.id,
                'name': profile.full_name or u.username if profile else u.username,
                'email': u.email,
                'role': profile.role if profile else 'user',
                'phone': profile.phone if profile else '',
                'dob': profile.dob if profile else '',
                'gender': profile.gender if profile else '',
                'address': profile.address if profile else '',
                'emergency_contact': profile.emergency_contact if profile else '',
                'reportCount': u.report_count,
                'status': 'Active' if u.is_active else 'Blocked',
                'lastActivity': u.last_report or u.last_login or 'New User'
            })
        return Response(data)

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'
    
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data
        
        if 'name' in data and hasattr(user, 'profile'):
            user.profile.full_name = data['name']
            user.profile.save()
            
        if 'email' in data:
            user.email = data['email']
            user.username = data['email'] # Assuming email is username
            
        if 'status' in data:
            user.is_active = (data['status'] == 'Active')
            
        user.save()
        return Response({'success': True})

class GlobalReportsView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    
    def get(self, request):
        from reports.models import ClinicalData
        
        assessments = HealthAssessment.objects.select_related('user__profile').order_by('-timestamp').all()
        vitals = ClinicalData.objects.select_related('patient__user__profile').order_by('-timestamp').all()
        
        data = []
        for a in assessments:
            data.append({
                'id': f"AI-{a.id}",
                'module': a.get_assessment_type_display(),
                'userName': a.user.profile.full_name or a.user.username if hasattr(a.user, 'profile') else a.user.username,
                'risk': a.results.get('riskLevel', 'Normal'),
                'timestamp': a.timestamp,
                'details': a.inputs,
                'results': a.results
            })
            
        for v in vitals:
            data.append({
                'id': f"VT-{v.id}",
                'module': 'Clinical Vitals',
                'userName': v.patient.user.profile.full_name or v.patient.user.username if hasattr(v.patient.user, 'profile') else v.patient.user.username,
                'risk': 'Clinical Entry',
                'timestamp': v.timestamp,
                'details': {
                    'Weight': v.weight,
                    'Height': v.height,
                    'BMI': v.bmi,
                    'BP': f"{v.blood_pressure_sys}/{v.blood_pressure_dia}",
                    'Heart Rate': v.heart_rate,
                    'SpO2': v.spo2
                },
                'results': {}
            })
            
        # Sort by timestamp descending
        data.sort(key=lambda x: x['timestamp'], reverse=True)
        return Response(data)
