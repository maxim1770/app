from fastapi import APIRouter

from app.api.api_v1.endpoints.saint import saint

router = APIRouter()

router.include_router(saint.router)
