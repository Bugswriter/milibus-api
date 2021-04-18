import uvicorn
from fastapi import FastAPI, Request
from app.db.init_db import init_db
from app.api.v1.api import api_router

app = FastAPI(title="Milibus API", debug=True)
init_db()


app.include_router(api_router, prefix="/v1")
