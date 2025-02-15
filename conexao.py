from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from dotenv import load_dotenv
import os

try:
    load_dotenv()
    db_url = os.getenv('DB_URL')
    DATABASE_URL = db_url

    engine = create_engine(DATABASE_URL)

    Session = sessionmaker(bind=engine)
    session = Session()

    print("\n ---- conexão realizada com sucesso ---- \n")
except Exception as e:
    print(f"\n !! Erro ao conectar: {e} !! \n")

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)