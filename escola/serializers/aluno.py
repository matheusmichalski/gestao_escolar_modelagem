from escola.models import Aluno

from rest_framework.serializers import ModelSerializer


class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"
