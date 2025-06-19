from escola.models import Projeto_Extracurricular

from rest_framework.serializers import ModelSerializer


class Projeto_ExtracurricularSerializer(ModelSerializer):
    class Meta:
        model = Projeto_Extracurricular
        fields = "__all__"
