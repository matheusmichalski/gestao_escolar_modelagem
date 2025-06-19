from escola.models import Turma

from rest_framework.serializers import ModelSerializer


class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = "__all__"
