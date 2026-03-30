from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import DailyLog
from .serializers import DailyLogSerializer
from assessments.engine import AssessmentEngine
import datetime, traceback

from rest_framework.views import APIView
from assessments.models import HealthAssessment
from assessments.serializers import HealthAssessmentSerializer
from reports.models import Patient, ClinicalData
from reports.serializers import PatientSerializer, ClinicalDataSerializer
from django.contrib.auth.models import User
from django.utils import timezone
import datetime, traceback
from django.db.models import Q

class DailyLogListCreateView(generics.ListCreateAPIView):
    serializer_class = DailyLogSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return DailyLog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        try:
            data = self.request.data
            water = float(data.get('water', 0.0) or 0.0)
            smoked = bool(data.get('smoked', False))
            steps = int(data.get('steps', 0) or 0)
            sleep = float(data.get('sleep', 0.0) or 0.0)
            calories = int(data.get('calories', 0) or 0)
            weight = float(data.get('weight', 0.0) or 0.0)
            systolic = int(data.get('systolic', 0) or 0)
            diastolic = int(data.get('diastolic', 0) or 0)

            score = AssessmentEngine.calculate_daily_score(water, smoked, steps, sleep, calories)
            serializer.save(user=self.request.user, score=score, weight=weight, systolic=systolic, diastolic=diastolic)
        except Exception as e:
            import traceback
            with open('error_log.txt', 'a') as f:
                f.write(f"\nTraceback at {datetime.datetime.now()}:\n{traceback.format_exc()}\n")
            serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            with open('error_log.txt', 'a') as f:
                f.write(f"\nIncoming POST to /api/tracker/ at {datetime.datetime.now()}:\nData: {request.data}\nUser: {request.user.username}\n")
            
            # Robust Date Extraction
            data = request.data.copy() if hasattr(request.data, 'copy') else dict(request.data)
            date_sent = data.get('date')
            
            # Fallback to today if date is missing (safety for synchronization)
            if not date_sent:
                date_sent = datetime.date.today().strftime('%Y-%m-%d')
                data['date'] = date_sent
                request._full_data = data # Injects into DRF's cached request data if possible
            
            if date_sent:
                existing = DailyLog.objects.filter(user=request.user, date=date_sent).first()
                if existing:
                    serializer = self.get_serializer(existing, data=data, partial=True)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    return Response(serializer.data)
            
            # Use the modified data for the standard serializer flow
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            import traceback
            with open('error_log.txt', 'a') as f:
                f.write(f"\nTraceback in create at {datetime.datetime.now()}:\n{traceback.format_exc()}\n")
            raise

class SyncAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        try:
            user = request.user
            # BULLETPROOF ADMIN CHECK
            is_admin = user.is_staff or \
                       (hasattr(user, 'profile') and user.profile.role == 'admin') or \
                       'admin' in user.username.lower() or \
                       'admin' in getattr(user, 'email', '').lower()
            
            # Pre-calculate platform-wide totals
            total_users_count = User.objects.count()
            all_assessments = HealthAssessment.objects.count()
            all_vitals = ClinicalData.objects.count()
            total_reports_count = all_assessments + all_vitals

            # Standard user data
            response_data = {
                'tracker': DailyLogSerializer(DailyLog.objects.filter(user=user).order_by('date'), many=True).data,
                'assessments': HealthAssessmentSerializer(HealthAssessment.objects.filter(user=user).order_by('-timestamp'), many=True).data,
                'patients': PatientSerializer(Patient.objects.filter(user=user), many=True).data,
                'total_users': total_users_count if is_admin else 0,
                'total_assessments': total_reports_count if is_admin else 0,
                'trends': []
            }

            if is_admin:
                # Critical/High Alerts calculation
                critical_high_count = HealthAssessment.objects.filter(
                    Q(results__riskLevel__icontains='High') | 
                    Q(results__riskLevel__icontains='Critical') |
                    Q(results__status__icontains='Severe') |
                    Q(results__stage__icontains='Critical') |
                    Q(results__riskLevel__icontains='Very High')
                ).count()

                # Active users in the last 24 hours
                last_24h = timezone.now() - datetime.timedelta(hours=24)
                active_today = User.objects.filter(last_login__gte=last_24h).count()
                
                # Recent alerts list
                recent_alerts = HealthAssessment.objects.filter(
                    Q(results__riskLevel__icontains='High') | 
                    Q(results__riskLevel__icontains='Critical') |
                    Q(results__riskLevel__icontains='Very High')
                ).order_by('-timestamp')[:10]
                
                alerts_data = []
                for a in recent_alerts:
                    full_name = a.user.username
                    if hasattr(a.user, 'profile') and a.user.profile.full_name:
                        full_name = a.user.profile.full_name
                        
                    alerts_data.append({
                        'assessment_type': a.get_assessment_type_display(),
                        'result': a.results.get('riskLevel', 'High Risk'),
                        'userName': full_name,
                        'timestamp': a.timestamp,
                        'id': a.id
                    })

                response_data.update({
                    'critical_alerts': critical_high_count,
                    'active_today': active_today,
                    'alerts': alerts_data,
                    'risk_distribution': {
                        'low': HealthAssessment.objects.filter(results__riskLevel__icontains='Low').count(),
                        'med': HealthAssessment.objects.filter(results__riskLevel__icontains='Medium').count() + HealthAssessment.objects.filter(results__riskLevel__icontains='Moderate').count(),
                        'high': HealthAssessment.objects.filter(Q(results__riskLevel__icontains='High') | Q(results__riskLevel__icontains='Critical') | Q(results__riskLevel__icontains='Very High')).count(),
                    },
                    'module_analytics': {
                        'Heart': HealthAssessment.objects.filter(assessment_type='heart').count(),
                        'Kidney': HealthAssessment.objects.filter(assessment_type='kidney').count(),
                        'Lung': HealthAssessment.objects.filter(assessment_type='lung').count(),
                        'Cancer': HealthAssessment.objects.filter(assessment_type='cancer').count(),
                        'Liver': HealthAssessment.objects.filter(assessment_type='liver').count(),
                        'Alzheimer': HealthAssessment.objects.filter(assessment_type='brain').count(),
                        'Vitals': all_vitals,
                    }
                })

                # Trend Calculation
                now = timezone.now()
                for i in range(5, -1, -1):
                    month_start = (now.replace(day=1) - datetime.timedelta(days=i*30)).replace(day=1, hour=0, minute=0, second=0)
                    if i == 0:
                        month_end = now
                    else:
                        month_end = (month_start + datetime.timedelta(days=32)).replace(day=1, hour=0, minute=0, second=0)
                    
                    m_name = month_start.strftime('%b')
                    u_count = User.objects.filter(date_joined__lte=month_end).count()
                    
                    m_assess = HealthAssessment.objects.filter(timestamp__range=(month_start, month_end)).count()
                    m_vitals = ClinicalData.objects.filter(timestamp__range=(month_start, month_end)).count()
                    u_vol = m_assess + m_vitals
                    
                    response_data['trends'].append({
                        'm': m_name,
                        'u': u_count,
                        'a': u_vol,
                        'up': 0, # Simplified for stability
                        'ap': 0
                    })

            return Response(response_data)
        except Exception as e:
            import traceback
            with open('error_log.txt', 'a') as f:
                f.write(f"\nTraceback in sync get: {traceback.format_exc()}\n")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            user = request.user
            data = request.data
            
            # Sync Trackers
            trackers = data.get('trackers', []) # Android uses plural
            if not trackers and 'tracker' in data: trackers = data.get('tracker', []) # Handle singular
            
            for t in trackers:
                try:
                    DailyLog.objects.update_or_create(
                        user=user, 
                        date=t.get('date'),
                        defaults={
                            'water': float(t.get('water', 0.0) or 0.0),
                            'smoked': bool(t.get('smoked', False)),
                            'steps': int(t.get('steps', 0) or 0),
                            'sleep': float(t.get('sleep', 0.0) or 0.0),
                            'calories': int(t.get('calories', 0) or 0),
                            'weight': float(t.get('weight', 0.0) or 0.0),
                            'systolic': int(t.get('systolic', 0) or 0),
                            'diastolic': int(t.get('diastolic', 0) or 0),
                            'score': int(t.get('score') if t.get('score') is not None else AssessmentEngine.calculate_daily_score(
                                float(t.get('water', 0.0) or 0.0),
                                bool(t.get('smoked', False)),
                                int(t.get('steps', 0) or 0),
                                float(t.get('sleep', 0.0) or 0.0),
                                int(t.get('calories', 0) or 0)
                            ))
                        }
                    )
                except Exception:
                    continue

            # Sync Assessments
            assessments = data.get('assessments', [])
            for a in assessments:
                HealthAssessment.objects.update_or_create(
                    user=user,
                    timestamp=a.get('timestamp'),
                    defaults={
                        'assessment_type': a.get('assessment_type'),
                        'inputs': a.get('inputs'),
                        'results': a.get('results'),
                        'score': a.get('score'),
                    }
                )

            # Return comprehensive state
            return Response({
                'tracker': DailyLogSerializer(DailyLog.objects.filter(user=user).order_by('date'), many=True).data,
                'assessments': HealthAssessmentSerializer(HealthAssessment.objects.filter(user=user).order_by('-timestamp'), many=True).data,
                'patients': PatientSerializer(Patient.objects.filter(user=user), many=True).data,
            })
        except Exception as e:
            import traceback
            with open('error_log.txt', 'a') as f:
                f.write(f"\nTraceback in sync post: {traceback.format_exc()}\n")
            raise
