from rest_framework import serializers
from escola.models import Avaliacao, Disciplina


class AvaliacaoSerializer(serializers.ModelSerializer):
    disciplina = serializers.PrimaryKeyRelatedField(queryset=Disciplina.objects.all())

    class Meta:
        model = Avaliacao
        fields = "__all__"
