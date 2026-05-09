from fastapi import APIRouter
from api.v1.endpoints import student


api_router = APIRouter()
api_router.include_router(student.router, prefix='/school', tags=['schooll'])