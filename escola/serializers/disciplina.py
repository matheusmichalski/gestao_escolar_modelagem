from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from escola.models.professor import Professor
from escola.models import Disciplina


class DisciplinaSerializer(ModelSerializer):
    professores = serializers.SlugRelatedField(
        many=True,
        queryset=Professor.objects.all(),
        slug_field="nome",
    )
    avaliacoes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="tema",
    )

    class Meta:
        model = Disciplina
        fields = "__all__"
