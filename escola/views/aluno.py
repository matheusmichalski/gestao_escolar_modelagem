from rest_framework.viewsets import ModelViewSet
from escola.models import Aluno
from escola.serializers import AlunoSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer