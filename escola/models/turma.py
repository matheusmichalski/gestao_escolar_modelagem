from django.db import models
import uuid


class Turma(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    num_alunos = models.IntegerField(null=False)
    data_inicio = models.DateField(auto_now=False, blank=False, null=False)
    data_termino = models.DateField(auto_now=False, blank=False, null=False)
    matriculas = models.ForeignKey("escola.Matricula", on_delete=models.CASCADE)
