from django.db import models
import uuid


class Turma(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    curso = models.ForeignKey(
        "escola.Curso", on_delete=models.CASCADE, related_name="turmas"
    )
    num_turma = models.IntegerField(null=False)
    num_alunos = models.IntegerField(null=False)
    data_inicio = models.DateField(auto_now=False, blank=False, null=False)
    data_termino = models.DateField(auto_now=False, blank=False, null=False)
    matriculas = models.ForeignKey(
        "escola.Matricula", on_delete=models.CASCADE, related_name="matriculas"
    )
    curso = models.ForeignKey(
        "escola.Curso", on_delete=models.CASCADE, related_name="curso"
    )

    def __str__(self):
        return f"{self.curso}{self.num_turma}"
