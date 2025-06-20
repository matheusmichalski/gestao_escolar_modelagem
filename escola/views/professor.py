from rest_framework.viewsets import ModelViewSet
from escola.models import Professor
from escola.serializers import ProfessorSerializer

class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer