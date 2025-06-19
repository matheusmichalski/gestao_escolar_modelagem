from django.contrib import admin
from .models import (
    Aluno,
    Matricula,
    Turma,
    Curso,
    Disciplina,
    Avaliacao,
    Professor,
    Projeto_Extracurricular,
    Bolsa_Pesquisa,
)

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Matricula)
admin.site.register(Turma)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Avaliacao)
admin.site.register(Professor)
admin.site.register(Projeto_Extracurricular)
admin.site.register(Bolsa_Pesquisa)
