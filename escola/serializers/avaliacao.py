from escola.models import Avaliacao

from rest_framework.serializers import ModelSerializer


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"
