from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from escola.views.aluno import AlunoViewSet
from escola.views.avaliacao import AvaliacaoViewSet
from escola.views.bolsa_pesquisa import Bolsa_PesquisaViewSet
from escola.views.curso import CursoViewSet
from escola.views.disciplina import DisciplinaViewSet
from escola.views.frequencia import FrequenciaViewSet
from escola.views.matricula import MatriculaViewSet
from escola.views.professor import ProfessorViewSet
from escola.views.projeto_extracurricular import Projeto_ExtracurricularViewSet
from escola.views.turma import TurmaViewSet

router = DefaultRouter()
router.register(r"alunos", AlunoViewSet)
router.register(r"avaliacoes", AvaliacaoViewSet)
router.register(r"bolsas-pesquisa", Bolsa_PesquisaViewSet)
router.register(r"cursos", CursoViewSet)
router.register(r"disciplinas", DisciplinaViewSet)
router.register(r"frequencias", FrequenciaViewSet)
router.register(r"matriculas", MatriculaViewSet)
router.register(r"professores", ProfessorViewSet)
router.register(r"projetos-extracurriculares", Projeto_ExtracurricularViewSet)
router.register(r"turmas", TurmaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
