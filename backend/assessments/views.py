from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import HealthAssessment
from .engine import AssessmentEngine
from .serializers import HealthAssessmentSerializer

class HealthAssessmentListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = HealthAssessmentSerializer

    def get_queryset(self):
        return HealthAssessment.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        data = request.data
        assessment_type = data.get('assessment_type')
        inputs = data.get('inputs')

        if not assessment_type or not inputs:
            return Response({"error": "Type and inputs are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            results = {}
            if assessment_type == 'kidney':
                results = AssessmentEngine.calculate_kidney(
                    float(inputs.get('gfr', 0.0)),
                    bool(inputs.get('protein_present', False))
                )
            elif assessment_type == 'heart':
                results = AssessmentEngine.calculate_heart(
                    int(inputs.get('systolic', 0)),
                    int(inputs.get('diastolic', 0)),
                    int(inputs.get('cholesterol', 0)),
                    int(inputs.get('ldl', 0)),
                    int(inputs.get('sugar', 0)),
                    bool(inputs.get('abnormal_ecg', False))
                )
            elif assessment_type == 'liver':
                results = AssessmentEngine.calculate_liver(
                    float(inputs.get('alt', 0)),
                    float(inputs.get('ast', 0)),
                    float(inputs.get('bilirubin', 0.0)),
                    float(inputs.get('albumin', 0.0)),
                    float(inputs.get('alp', 0))
                )
            elif assessment_type == 'lung':
                results = AssessmentEngine.calculate_lung(
                    float(inputs.get('fev1', 0.0)),
                    float(inputs.get('ratio', 0.0)),
                    float(inputs.get('spo2', 0.0)),
                    bool(inputs.get('is_smoker', False))
                )
            elif assessment_type == 'cancer':
                results = AssessmentEngine.calculate_cancer(
                    str(inputs.get('tumor_size', 'T1')),
                    bool(inputs.get('lymph_node', False)),
                    bool(inputs.get('metastasis', False)),
                    str(inputs.get('biopsy_grade', 'Low'))
                )
            elif assessment_type == 'brain':
                results = AssessmentEngine.calculate_brain(
                    int(inputs.get('mmse', 0)),
                    int(inputs.get('age', 0)),
                    str(inputs.get('clinical', '')),
                    bool(inputs.get('family_history', False))
                )
            else:
                return Response({"error": "Invalid assessment type"}, status=status.HTTP_400_BAD_REQUEST)

            score = results.get('score', 0)

            assessment = HealthAssessment.objects.create(
                user=request.user,
                assessment_type=assessment_type,
                inputs=inputs,
                results=results,
                score=score
            )
            serializer = self.get_serializer(assessment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HealthAssessmentDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = HealthAssessmentSerializer

    def get_queryset(self):
        return HealthAssessment.objects.filter(user=self.request.user)
