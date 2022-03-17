from typing import Optional  # essa classe diz que algum parametro nao é obrigatorio

from fastapi import FastAPI  # importando o FastAPI

app = FastAPI()


# diz que funcao abaixo é responsavel por ler dados da "rota" (URL),   "get" é o nome da operacao
@app.get("/")
async def root():  # função assincrona
    return {"message": "Hello World"}


# item_id e q : parametros que serão mostrados na documentacao
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

    # Em seguida executar : uvicorn main:app --reload : mostra a URL onde a aplicacao foi desenvolvida
