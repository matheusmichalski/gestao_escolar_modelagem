from django.db import models
import datetime
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

    def save(self, *args, **kwargs):
        if not self.registration_code:
            year = datetime.now().year
            sequence_name = f"registration_{year}"
            sequence_number = get_next_value(sequence_name)
            formated_number = str(sequence_number).zfill(6)
            self.registration_code = f"{year}{formated_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.registration_code
