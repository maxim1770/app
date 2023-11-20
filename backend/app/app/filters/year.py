from fastapi_filter.contrib.sqlalchemy import Filter

from app import models


class YearFilter(Filter):
    year__gte: int | None = None
    year__lt: int | None = None

    class Constants(Filter.Constants):
        model = models.Year
