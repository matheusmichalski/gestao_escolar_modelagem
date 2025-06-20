from django.db import models
from django.utils import timezone
from sequences import get_next_value


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
        blank=False,
    )
    status = models.CharField(
        choices=STATUS_MATRICULA, max_length=1, blank=False, null=False, default="P"
    )
    aluno = models.OneToOneField(
        "escola.aluno", on_delete=models.PROTECT, related_name="aluno"
    )

    curso = models.ForeignKey(
        "escola.Curso", on_delete=models.PROTECT, related_name="matriculas"
    )

    def save(self, *args, **kwargs):
        if not self.num_matricula:
            year = timezone.now().year
            sequence_name = f"registration_{year}"
            sequence_number = get_next_value(sequence_name)
            formated_number = str(sequence_number).zfill(6)
            self.num_matricula = f"{year}{formated_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.num_matricula
