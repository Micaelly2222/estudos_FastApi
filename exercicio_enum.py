# Usando declaraçoes do tipo Python
# Criando classe Enum: valores do parâmetro da rota ser predefinidos

from enum import Enum  # importando Enum

from fastapi import FastAPI


class ModelName(str, Enum):  # criar uma classe com str e enum
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
# funcao usando a classe criada(model name)
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:  # comparando membros do Enum
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":  # valor exato do enumerate
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

    # comando: python -m uvicorn exercicio_enum:app
    # http://127.0.0.1:8000/docs
