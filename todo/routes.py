from fastapi import Request, Depends
from sqlalchemy.orm import Session
from todo.config import settings
from todo.main import app,templates
from todo.database.base import get_db
from todo.models import ToDo

@app.get('/')
def home(request: Request, db_session: Session = Depends(get_db)):
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'todo_list': todos})


