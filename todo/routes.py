from fastapi import Request
from todo.main import app,templates


@app.get('/')
def home(request: Request):
    return {'one': 1}


