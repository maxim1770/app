from fastapi_filter.contrib.sqlalchemy import Filter

from app import models


class DayFilter(Filter):
    month: int | None = None
    day: int | None = None

    class Constants(Filter.Constants):
        model = models.Day
