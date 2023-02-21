from todo.database.base import Base
from sqlalchemy import Column, String, Boolean, Integer


class ToDo(Base):
    __tablename__='todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column (String)
    is_complete = Column(Boolean, default=False)
