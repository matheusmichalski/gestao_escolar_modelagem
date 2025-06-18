from django.db import models
import uuid


class Frequencia(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    data_aula = models.DateField(auto_now=True, blank=False, null=False)
    ementa = models.CharField(max_length=255)
