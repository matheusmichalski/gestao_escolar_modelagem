from escola.models import Bolsa_Pesquisa

from rest_framework.serializers import ModelSerializer


class Bolsa_PesquisaSerializer(ModelSerializer):
    class Meta:
        model = Bolsa_Pesquisa
        fields = "__all__"
