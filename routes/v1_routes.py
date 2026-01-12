from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from controllers.libro_controller import get_libro
from schemas.libro_schema import LibroV1

router = APIRouter(tags=["Libros v1"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/libros/{libro_id}", response_model=LibroV1, deprecated=True)
def read_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = get_libro(db, libro_id)
    return libro
