from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def root_get():
    return "Hello World"

@app.post("/")
def root_post():
    return {"msg": "pong"}
