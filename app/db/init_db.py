from app.models import buses
from app.db.database import engine

def init_db():
  buses.Base.metadata.create_all(bind=engine)
