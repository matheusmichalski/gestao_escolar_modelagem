from escola.models import Disciplina
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class DisciplinaSerializer(ModelSerializer):
    professores = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="nome"
    )
    avaliacoes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="nome"
    )

    class Meta:
        model = Disciplina
        fields = "__all__"
