from fastapi import APIRouter

from app.api.api_v1.endpoints.movable_date import cycles

router = APIRouter()

router.include_router(cycles.router)
