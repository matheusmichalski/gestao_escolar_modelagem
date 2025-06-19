from escola.models import Matricula

from rest_framework.serializers import ModelSerializer


class MatriculaSerializer(ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"
