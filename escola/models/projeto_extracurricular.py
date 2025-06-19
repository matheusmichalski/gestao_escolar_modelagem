from django.db import models
import uuid


class Projeto_Extracurricular(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    ementa = models.CharField(max_length=500)
    data_inicio = models.DateField(auto_now=False, blank=False, null=False)
    data_termino = models.DateField(auto_now=False, blank=True, null=True)
    professor_orientador = models.ForeignKey(
        "escola.Professor",
        on_delete=models.PROTECT,
        related_name="projeto_extracurricular",
    )
