from django.db import models
import uuid


class Bolsa_Pesquisa(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    data_inicio = models.DateField(auto_now=False, blank=False, null=False)
    data_termino = models.DateField(auto_now=False, blank=True, null=True)
    projeto_extracurricular = models.ForeignKey(
        "escola.Projeto_Extracurricular",
        on_delete=models.PROTECT,
        related_name="bolsa_pesquisa",
    )

    def __str__(self):
        return str(self.projeto_extracurricular)
