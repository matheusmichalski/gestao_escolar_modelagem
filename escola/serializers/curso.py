from escola.models import Curso

from rest_framework.serializers import ModelSerializer


class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"
