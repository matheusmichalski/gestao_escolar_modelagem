from rest_framework.viewsets import ModelViewSet
from escola.models import Projeto_Extracurricular
from escola.serializers import Projeto_ExtracurricularSerializer

class Projeto_ExtracurricularViewSet(ModelViewSet):
    queryset = Projeto_Extracurricular.objects.all()
    serializer_class = Projeto_ExtracurricularSerializer