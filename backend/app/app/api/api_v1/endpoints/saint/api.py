from fastapi import APIRouter

from app.api.api_v1.endpoints.saint import saints

router = APIRouter()

router.include_router(saints.router)
