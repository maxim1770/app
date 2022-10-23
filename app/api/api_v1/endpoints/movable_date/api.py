from fastapi import APIRouter

from app.api.api_v1.endpoints.movable_date import day, week, cycle

week.router.include_router(day.router, prefix='/{sunday_num}/days')

cycle.router.include_router(week.router, prefix='/{cycle_num}/weeks')

router = APIRouter()

router.include_router(cycle.router)
