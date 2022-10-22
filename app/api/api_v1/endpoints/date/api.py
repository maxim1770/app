from fastapi import APIRouter

from app.api.api_v1.endpoints.date import day, week, period

week.router.include_router(day.router, prefix='/days')

period.router.include_router(week.router, prefix='/weeks')

router = APIRouter()

router.include_router(period.router)
