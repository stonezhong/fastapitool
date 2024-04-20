from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from demo.core.models import Base
from sqlalchemy.orm import Session

engine = create_engine(f"sqlite:///foo.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)

def db_factory() -> Session:
    return SessionLocal()
