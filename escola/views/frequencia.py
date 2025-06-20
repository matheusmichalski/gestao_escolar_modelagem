from rest_framework.viewsets import ModelViewSet
from escola.models import Frequencia
from escola.serializers import FrequenciaSerializer

class FrequenciaViewSet(ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer