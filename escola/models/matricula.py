from django.db import models
from django.utils import timezone
from sequences import get_next_value
from django.core.exceptions import ValidationError
from escola.models.aluno import Aluno


class Matricula(models.Model):
    STATUS_MATRICULA = (
        ("A", "Ativa"),
        ("I", "Inativa"),
        ("P", "Pendente"),
    )

    num_matricula = models.CharField(
        primary_key=True,
        max_length=10,
        unique=True,
        editable=False,
    )
    status = models.CharField(
        choices=STATUS_MATRICULA,
        max_length=1,
        default="P",
    )
    aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, related_name="matriculas"
    )
    curso = models.ForeignKey(
        "escola.Curso", on_delete=models.PROTECT, related_name="matriculas"
    )
    turma = models.ForeignKey(
        "escola.Turma",
        on_delete=models.CASCADE,
        related_name="matriculas",
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["aluno"], name="unique_matricula_por_aluno")
        ]

    def clean(self):
        super().clean()

        if self.turma and self.curso:
            if self.turma.curso_id != self.curso_id:
                raise ValidationError(
                    {"turma": "A turma selecionada não pertence ao curso informado."}
                )

    def save(self, *args, **kwargs):
        self.full_clean()

        if self.pk:
            original = Matricula.objects.get(pk=self.pk)
            if self.num_matricula != original.num_matricula:
                raise ValidationError("O número da matrícula não pode ser alterado.")
        else:
            year = timezone.now().year
            sequence_name = f"registration_{year}"
            sequence_number = get_next_value(sequence_name)
            formated_number = str(sequence_number).zfill(6)
            self.num_matricula = f"{year}{formated_number}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.num_matricula
