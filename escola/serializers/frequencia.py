from escola.models import Frequencia

from rest_framework.serializers import ModelSerializer


class FrequenciaSerializer(ModelSerializer):
    class Meta:
        model = Frequencia
        fields = "__all__"
