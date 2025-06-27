from django.db import models
from escola.models import Curso
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import uuid


class Disciplina(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(null=False, validators=[MinValueValidator(1)])
    ementa = models.CharField(max_length=500)
    professores = models.ManyToManyField("escola.Professor", related_name="disciplinas")

    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()

        cursos = Curso.objects.filter(disciplinas=self)
        for curso in cursos:
            if self.carga_horaria > curso.carga_horaria:
                raise ValidationError(
                    f"A carga horária da disciplina ({self.carga_horaria}h) "
                    f"não pode ser maior que a do curso '{curso.nome}' ({curso.carga_horaria}h)."
                )
