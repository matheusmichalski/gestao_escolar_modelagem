from rest_framework.viewsets import ModelViewSet
from escola.models import Avaliacao
from escola.serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer