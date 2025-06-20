from rest_framework.viewsets import ModelViewSet
from escola.models import Bolsa_Pesquisa
from escola.serializers import Bolsa_PesquisaSerializer

class Bolsa_PesquisaViewSet(ModelViewSet):
    queryset = Bolsa_Pesquisa.objects.all()
    serializer_class = Bolsa_PesquisaSerializer