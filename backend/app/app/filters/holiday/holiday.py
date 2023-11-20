from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from app import models
from .holiday_category import HolidayCategoryFilter
from .tipikon import TipikonFilter
from ..day import DayFilter


class HolidayFilter(Filter):
    holiday_category: HolidayCategoryFilter | None = FilterDepends(
        with_prefix('holiday_category', HolidayCategoryFilter)
    )
    tipikon: TipikonFilter | None = FilterDepends(
        with_prefix('tipikon', TipikonFilter)
    )
    day: DayFilter | None = FilterDepends(
        with_prefix('day', DayFilter)
    )

    search: str | None = None

    order_by: list[str] = ['tipikon_id']

    class Constants(Filter.Constants):
        model = models.Holiday
        search_model_fields = ['title', 'slug']
