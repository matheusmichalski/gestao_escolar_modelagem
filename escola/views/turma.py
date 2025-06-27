from rest_framework.viewsets import ModelViewSet
from escola.models import Turma
from escola.serializers import TurmaSerializer


class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
