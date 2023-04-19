from fastapi_filter.contrib.sqlalchemy import Filter

from app import models


class YearFilter(Filter):
    year__gte: int | None
    year__lt: int | None
    order_by: list[str] = ['year']

    class Constants(Filter.Constants):
        model = models.Year
