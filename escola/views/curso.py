from rest_framework.viewsets import ModelViewSet
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer