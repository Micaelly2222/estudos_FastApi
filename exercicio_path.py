from fastapi import FastAPI  # importando o FastAPI

app = FastAPI()


@app.get("/items/{item_id}")  # a rota
# item_id está sendo declarado como um int., muda na documentacao
async def read_item(item_id: int):
    return {"item_id": item_id}  # vai retornar um valor inteiro
