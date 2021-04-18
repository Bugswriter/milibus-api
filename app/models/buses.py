from sqlalchemy import Column, String, Integer
from app.db.database import Base

class Buses(Base):
  __tablename__ = "buses"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  plate = Column(String, index=True)
  code = Column(String, index=True)
