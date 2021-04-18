from pydantic import BaseModel

class Buses(BaseModel):
  name: str
  plate: str
  code: str

  class Config:
    orm_mode = True
