from fastapi import APIRouter

from app.api.api_v1.endpoints.holiday import holidays

router = APIRouter()

router.include_router(holidays.router)
