from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.config_variables import settings

engine = create_engine(
    settings.database_url, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

from sqlalchemy.orm import Session
from models.libro_model import Libro

def init_db():
    db: Session = SessionLocal()
    libros_iniciales = [
        {"id": 1, "titulo": "Clean Code", "autor": "Robert C. Martin"},
        {"id": 2, "titulo": "The Pragmatic Programmer", "autor": "Andrew Hunt"},
        {"id": 3, "titulo": "Design Patterns", "autor": "Erich Gamma"},
        {"id": 4, "titulo": "Maths", "autor": "Jonathan"},
    ]
    for libro_dict in libros_iniciales:
        libro_existente = db.query(Libro).filter(Libro.id == libro_dict["id"]).first()
        if not libro_existente:
            libro = Libro(**libro_dict)
            db.add(libro)
    db.commit()
    db.close()

