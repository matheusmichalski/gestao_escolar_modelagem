from django.db import models
import uuid


class Turma(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    curso = models.ForeignKey(
        "escola.Curso", on_delete=models.CASCADE, related_name="turmas"
    )
    num_turma = models.IntegerField(null=False, blank=True)
    data_inicio = models.DateField(auto_now=False, blank=False, null=False)
    data_termino = models.DateField(auto_now=False, blank=False, null=False)
    curso = models.ForeignKey(
        "escola.Curso", on_delete=models.CASCADE, related_name="curso"
    )

    def save(self, *args, **kwargs):
        if not self.num_turma:
            maior_turma = (
                Turma.objects.filter(curso=self.curso)
                .aggregate(models.Max("num_turma"))
                .get("num_turma__max")
                or 0
            )
            self.num_turma = maior_turma + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.curso}-{self.num_turma}"
