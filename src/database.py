from sqlalchemy import create_engine
from config import DB
engine = create_engine(DB)

def get_connection():
    return engine.connect()