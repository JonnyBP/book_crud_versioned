from sqlalchemy.orm import Session
from models.libro_model import Libro

def get_libro(db: Session, libro_id: int):
    return db.query(Libro).filter(Libro.id == libro_id).first()
