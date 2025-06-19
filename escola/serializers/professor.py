from escola.models import Professor

from rest_framework.serializers import ModelSerializer


class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"
