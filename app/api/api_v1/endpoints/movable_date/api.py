from fastapi import APIRouter

from app.api.api_v1.endpoints.movable_date import movable_dates, movable_days, weeks, cycles

movable_days.router.include_router(movable_dates.router, prefix='/{movable_day_abbr}/{divine_service_title}')

weeks.router.include_router(movable_days.router, prefix='/sunday-{sunday_num}')

cycles.router.include_router(weeks.router, prefix='/cycle-{cycle_num}')

router = APIRouter()

router.include_router(cycles.router)
