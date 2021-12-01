import os
from sqlalchemy import Boolean, Column, Float, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
