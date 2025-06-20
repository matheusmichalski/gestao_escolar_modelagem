from rest_framework.viewsets import ModelViewSet
from escola.models import Disciplina
from escola.serializers import DisciplinaSerializer

class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer