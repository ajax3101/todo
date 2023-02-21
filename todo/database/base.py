import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(BASE_DIR, 'todo', 'database', 'DB')
if not os.path.exists(db_path):
    os.makedirs(db_path)

Base = declarative_base()

#engine = create_engine()