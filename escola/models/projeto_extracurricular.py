from django.db import models
import uuid


class Projeto_Extracurricular(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    titulo = models.CharField(max_length=100)
    ementa = models.CharField(max_length=500)
    data_inicio = models.DateField(auto_now=False, blank=False, null=False)
    data_termino = models.DateField(auto_now=False, blank=True, null=True)
    professor_orientador = models.ForeignKey(
        "escola.Professor",
        on_delete=models.PROTECT,
        related_name="projeto_extracurricular",
    )

    class Meta:
        verbose_name_plural = "Projetos_Extracurriculares"

    def __str__(self):
        return f"{self.titulo}, {self.professor_orientador}"
