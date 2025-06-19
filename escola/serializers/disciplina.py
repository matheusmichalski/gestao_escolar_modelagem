from escola.models import Disciplina

from rest_framework.serializers import ModelSerializer


class DisciplinaSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "__all__"
