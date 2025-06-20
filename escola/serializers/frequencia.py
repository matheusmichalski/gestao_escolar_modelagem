from escola.models import Frequencia
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from escola.models.matricula import Matricula


class FrequenciaSerializer(ModelSerializer):
    matricula = SlugRelatedField(
        slug_field="aluno__nome",
        queryset=Matricula.objects.all(),
    )

    class Meta:
        model = Frequencia
        fields = "__all__"
