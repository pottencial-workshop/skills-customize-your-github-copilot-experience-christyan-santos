# starter-code.py
# Código inicial para a tarefa: Construindo APIs REST com FastAPI

from fastapi import FastAPI

app = FastAPI()

tasks = []  # Lista de tarefas em memória

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de tarefas!"}

# Implemente os endpoints para /tasks conforme solicitado no README.md
