# pip install python-multipart
# Form: receber campos de formulario

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):  # enviar username e password
    return {"username": username}
