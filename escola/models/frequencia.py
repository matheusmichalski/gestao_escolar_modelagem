from django.db import models
import uuid


class Frequencia(models.Model):
    STATUS_CHOICES = [
        ("P", "Presente"),
        ("A", "Ausente"),
        ("J", "Justificado"),
    ]

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    data_aula = models.DateField(auto_now=True, blank=False, null=False)
    matricula = models.ForeignKey(
        "escola.Matricula", on_delete=models.CASCADE, related_name="frequencias"
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="A")
    obvervacoes = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.data_aula
