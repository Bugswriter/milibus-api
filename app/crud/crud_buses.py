from app.models.buses import Buses
from sqlalchemy.orm import Session
from app.schemas.buses import Buses as SchemaBuses

class CRUDBuses():
  def get(self, db: Session, bid):
    return db.query(Buses).filter(Buses.id == bid).first()


  def get_by_plate(self, db: Session, plate: str):
    return db.query(Buses).filter(Buses.plate == plate).first()


  def get_by_code(self, db: Session, code: str):
    return db.query(Buses).filter(Buses.code == code).first()


  def create_buses(self, db: Session, buses: SchemaBuses):
    db_buses = Buses(name=buses.name,plate=buses.plate,code=buses.code)
    db.add(db_buses)
    db.commit()
    db.refresh(db_buses)
    return db_buses


buses = CRUDBuses()
