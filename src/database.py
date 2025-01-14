import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, scoped_session
from sqlalchemy_mixins import AllFeaturesMixin
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL n'est pas défini dans le fichier .env")

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
SessionLocal = scoped_session(SessionFactory)


class Base(DeclarativeBase, AllFeaturesMixin):
    pass


Base.set_session(SessionLocal())
