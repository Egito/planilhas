from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()


# Configuração do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./idf.db")

# Criar engine do SQLAlchemy
# Configuração específica para SQLite
is_sqlite = DATABASE_URL.startswith("sqlite")
sqlite_args = {"check_same_thread": False} if is_sqlite else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=sqlite_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
