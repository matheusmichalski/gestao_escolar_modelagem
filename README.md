# Gestão Escolar — Modelagem

Projeto Django de modelagem de dados para um sistema de gestão escolar. Contém modelos, serializers e views organizados em um app chamado `escola`. O objetivo deste repositório é servir como base para estudos, protótipos ou ponto de partida para um sistema maior.

## Destaques

- Implementação de modelos para entidades escolares: alunos, professores, cursos, disciplinas, turmas, matrículas, frequência, avaliações e projetos extracurriculares.
- Estrutura modular com diretórios `models/`, `serializers/` e `views/` dentro do app `escola`.
- Histórico de migrações incluído (muitas mudanças iterativas nos modelos já registradas).

## Estrutura principal

Raiz do projeto:

- `manage.py` — utilitário do Django para executar comandos (migrations, runserver, etc.).
- `db.sqlite3` — banco de dados SQLite (para desenvolvimento/testes).
- `config/` — configurações do projeto Django (settings, urls, wsgi, asgi).
- `escola/` — app principal com modelos, serializers, views e migrações.

Dentro de `escola`:

- `models/` — definição das entidades (ex.: `aluno.py`, `professor.py`, `curso.py`, `turma.py`, ...).
- `serializers/` — serializers (provavelmente para uso com Django REST Framework).
- `views/` — views/handlers das APIs ou páginas.
- `migrations/` — histórico de alterações no schema do banco.

## Requisitos

O projeto usa Python (recomendado 3.11+) e Django. Dependências podem estar definidas em `pyproject.toml` e o ambiente local usa `__pypackages__/` (pdm/PEP 582) ou um virtualenv/venv.

Recomenda-se usar PDM ou criar um virtualenv e instalar dependências:

1. Com PDM (se estiver configurado):

```bash
# Instalar dependências (se for necessário)
pdm install
```

2. Com pip/venv:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # se existir
pip install -e .  # se o projeto for empacotado
```

Observação: se não houver `requirements.txt`, consulte `pyproject.toml` para dependências.

## Como executar (desenvolvimento)

1. Aplique as migrações (o projeto já tem um banco `db.sqlite3`, mas para reproduzir do zero):

```bash
python manage.py migrate
```

2. Crie um superusuário (opcional):

```bash
python manage.py createsuperuser
```

3. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

4. Acesse a aplicação localmente em `http://127.0.0.1:8000/`.

## Testes

Se existirem testes (padrão Django ou pytest), rode:

```bash
python manage.py test
# ou, se usar pytest:
pytest
```

## Boas práticas e notas

- O projeto já contém um histórico extenso de migrações; ao modificar modelos, gere novas migrações com `makemigrations`.
- Vale a pena revisar os serializers e views antes de expor APIs em produção.
- Para produção, substitua `db.sqlite3` por um banco mais robusto (Postgres) e ajuste `config/settings.py` (DEBUG, ALLOWED_HOSTS, SECRET_KEY e outras configurações de segurança).

## Contribuindo

1. Fork e branch feature: crie branches pequenos e atômicos.
2. Escreva testes para novas funcionalidades.
3. Abra pull requests com descrição clara do objetivo.

## Contato

Se precisar de ajuda com o repositório, abra uma issue descrevendo o que você quer fazer ou os problemas encontrados.

---

Este README foi gerado automaticamente para servir como resumo inicial; personalize-o com detalhes do seu domínio, scripts de execução específicos e instruções de deploy quando desejar.
