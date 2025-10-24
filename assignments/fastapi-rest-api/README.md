# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprender a criar uma API REST simples utilizando o framework FastAPI em Python. O estudante irá construir endpoints para manipular dados de uma lista de tarefas (to-do list).

## 📝 Tasks

### 🛠️ Criar Estrutura Básica da API

#### Description
Crie um arquivo Python que inicialize uma aplicação FastAPI e defina a rota raiz (`/`) que retorna uma mensagem de boas-vindas.

#### Requirements
Completed program should:
- Inicializar uma aplicação FastAPI
- Definir a rota `/` que retorna um JSON com uma mensagem de boas-vindas
- Rodar localmente usando `uvicorn`

### 🛠️ Endpoints para Gerenciar Tarefas

#### Description
Implemente endpoints para criar, listar, atualizar e remover tarefas de uma lista em memória.

#### Requirements
Completed program should:
- Definir um modelo de dados para tarefas (id, título, status)
- Implementar endpoint `GET /tasks` para listar todas as tarefas
- Implementar endpoint `POST /tasks` para adicionar uma nova tarefa
- Implementar endpoint `PUT /tasks/{id}` para atualizar uma tarefa existente
- Implementar endpoint `DELETE /tasks/{id}` para remover uma tarefa

---

Dica: Consulte a documentação oficial do FastAPI para exemplos e boas práticas: https://fastapi.tiangolo.com/
