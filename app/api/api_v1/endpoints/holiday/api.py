from fastapi import APIRouter

from app.api.api_v1.endpoints.holiday import holiday

router = APIRouter()

router.include_router(holiday.router)
