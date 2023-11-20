from fastapi_filter.contrib.sqlalchemy import Filter

from app import models


class DateFilter(Filter):
    year: int | None = None

    order_by: list[str] = []

    class Constants(Filter.Constants):
        model = models.Date
