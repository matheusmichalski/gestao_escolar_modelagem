from django.db import models

import uuid


class Curso(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(null=False)
    descricao = models.CharField(max_length=500)
    disciplinas = models.ManyToManyField(
        "escola.Disciplina", related_name="disciplinas"
    )

    def __str__(self):
        return self.nome
