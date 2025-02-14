from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
