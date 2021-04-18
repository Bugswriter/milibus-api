from fastapi import APIRouter, Depends
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from app.crud.crud_buses import buses as busescrud
from app.schemas.buses import Buses as SchemaBuses

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/")
def read_buses(code: str, db: Session=Depends(get_db)):
  if code:
    return busescrud.get_by_code(db=db, code=code)

  return buses

@router.post("/")
def create_buses(*, db: Session = Depends(get_db), buses: SchemaBuses):
  return busescrud.create_buses(db=db, buses=buses)
