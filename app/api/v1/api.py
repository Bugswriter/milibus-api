from fastapi import APIRouter
from app.api.v1.endpoints import buses

api_router = APIRouter()
api_router.include_router(buses.router, prefix="/buses", tags=["buses"])
