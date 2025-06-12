from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class Avaliacao(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    tipo = models.CharField(max_length=50)
    data = models.DateField(auto_now=True, blank=False, null=False)
    peso = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(10.00)],
    )
