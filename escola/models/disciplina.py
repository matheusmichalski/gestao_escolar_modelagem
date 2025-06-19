from django.db import models
import uuid

class Disciplina(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(null=False)
    ementa = models.CharField(max_length=500)
    professores = models.ManyToManyField("escola.Professor", related_name="professores")
    turmas = models.ManyToManyField("escola.Turma", related_name="turmas")
    avaliacoes = models.ManyToManyField("escola.Avaliacao", related_name="avaliacoes")

    def __str__(self):
        return self.nome
