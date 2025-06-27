from django.db import models
from django.core.exceptions import ValidationError
import uuid


class Turma(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    curso = models.ForeignKey(
        "escola.Curso", on_delete=models.CASCADE, related_name="turmas"
    )
    num_turma = models.IntegerField(null=False, blank=True)
    data_inicio = models.DateField(blank=False, null=False)
    data_termino = models.DateField(blank=False, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["curso", "num_turma"], name="unique_curso_num_turma"
            )
        ]

    def clean(self):
        # Validação de duplicidade
        if self.curso and self.num_turma:
            existe = (
                Turma.objects.exclude(pk=self.pk)
                .filter(curso=self.curso, num_turma=self.num_turma)
                .exists()
            )
            if existe:
                raise ValidationError(
                    "Já existe uma turma com esse número para este curso."
                )

        # Validação de datas
        if self.data_inicio and self.data_termino:
            if self.data_termino <= self.data_inicio:
                raise ValidationError(
                    "A data de término deve ser posterior à data de início."
                )

            dias = (self.data_termino - self.data_inicio).days + 1
            horas_disponiveis = dias * 24

            if self.curso and horas_disponiveis < self.curso.carga_horaria:
                raise ValidationError(
                    f"A duração da turma ({horas_disponiveis}h) é menor que a carga horária do curso ({self.curso.carga_horaria}h)."
                )

    def save(self, *args, **kwargs):
        self.full_clean()

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
        return f"{self.curso} - Turma {self.num_turma}"
