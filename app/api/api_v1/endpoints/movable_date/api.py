from fastapi import APIRouter

from app.api.api_v1.endpoints.movable_date import movable_date, movable_day, week, cycle

movable_day.router.include_router(movable_date.router, prefix='/{movable_day_abbr}/{divine_service_title}')

week.router.include_router(movable_day.router, prefix='/sunday-{sunday_num}')

cycle.router.include_router(week.router, prefix='/cycle-{cycle_num}')

router = APIRouter()

router.include_router(cycle.router)
