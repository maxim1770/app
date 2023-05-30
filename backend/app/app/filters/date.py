from fastapi_filter.contrib.sqlalchemy import Filter

from app import models


class DateFilter(Filter):
    search: str | None

    class Constants(Filter.Constants):
        model = models.Date
