from django.db import models
from localflavor.br.models import BRCPFField
import uuid


class Aluno(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    nome = models.CharField(
        max_length=45,
        blank=False,
        null=False,
    )
    cpf = BRCPFField(
        unique=True,
        blank=False,
        null=False,
    )
    data_nascimento = models.DateField(auto_now=False, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    telefone = models.CharField(max_length=20, blank=False, null=False)
