from rest_framework.viewsets import ModelViewSet
from escola.models import Matricula
from escola.serializers import MatriculaSerializer


class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
