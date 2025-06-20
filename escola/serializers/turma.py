from escola.models import Turma
from rest_framework import serializers

from rest_framework.serializers import ModelSerializer


class TurmaSerializer(serializers.ModelSerializer):
    curso = serializers.SerializerMethodField()

    class Meta:
        model = Turma
        fields = [
            "id",
            "num_turma",
            "data_inicio",
            "data_termino",
            "curso",
        ]

    def get_curso(self, obj):
        return f"{obj.curso.nome}-{obj.num_turma}"
