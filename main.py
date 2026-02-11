from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def root_get():
    return "Hello World"


@app.get("/quest")
def quest_get():
    return {"msg" : "pong"}