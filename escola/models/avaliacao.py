from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class Avaliacao(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    tema = models.CharField(max_length=50)
    data = models.DateField(
        blank=False,
        null=False,
    )
    peso = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],
    )
    disciplina = models.ForeignKey(
        "escola.Disciplina",
        on_delete=models.CASCADE,
        null=True,
        related_name="avaliacoes",
    )

    def __str__(self):
        return self.data.strftime("%d/%m/%Y")
