from escola.models import Matricula
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class MatriculaSerializer(ModelSerializer):
    curso = serializers.SlugRelatedField(
        read_only=True,
        slug_field="nome",
    )

    class Meta:
        model = Matricula
        fields = "__all__"
