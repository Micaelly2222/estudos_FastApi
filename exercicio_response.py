from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=200)  # retorna o codigo de status na resposta
async def create_item(name: str):
    return {"name": name}

# 100 "Informações"
# 200 respostas "Bem-sucedidas.
# 201 usado após a criação de um novo registro no banco de dados.
# 204 "Sem conteúdo".
# 300  "Redirecionamento".
# 400  "Erro do cliente".
# 500  erros do servidor.
