from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

current_path = Path(__file__).resolve()
parent_directory = current_path.parent.parent
db_uri = f"sqlite:///{parent_directory}/sql_app.sqlite3"

SQLALCHEMY_DATABASE_URL = db_uri


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
