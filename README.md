# 🎬 API Django REST Framework

API desenvolvida com **Django REST Framework** para gerenciamento de filmes.

## 📌 Sobre o projeto

A API permite cadastrar e gerenciar filmes, atores, gêneros e avaliações.

Também possui autenticação com **JWT** e alguns endpoints para consulta de estatísticas.

## ⚙️ Funcionalidades

* Cadastro, edição e exclusão de filmes
* Cadastro de atores e gêneros
* Sistema de avaliações de filmes
* Relacionamento entre filmes, atores e gêneros
* Autenticação com JWT
* Consulta de estatísticas

## 🛠️ Tecnologias

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite

## 🚀 Como executar

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd api-django-rest-framework
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

A API estará disponível em:

```text
http://127.0.0.1:8000/api/v1/
```

## 📚 Principais endpoints

| Recurso    | Endpoint              |
| ---------- | --------------------- |
| Filmes     | `/api/v1/filmes/`     |
| Atores     | `/api/v1/atores/`     |
| Gêneros    | `/api/v1/generos/`    |
| Avaliações | `/api/v1/avaliacoes/` |

## 🔐 Autenticação

A API utiliza **JWT** para autenticação.

Após obter o token, ele deve ser enviado nas requisições protegidas:

```text
Authorization: Bearer <seu-token>
```

## 🎯 Objetivo

Projeto desenvolvido para praticar **Django REST Framework, criação de APIs, autenticação, relacionamentos entre modelos e operações CRUD**.
