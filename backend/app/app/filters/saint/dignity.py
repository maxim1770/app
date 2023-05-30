from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums


class DignityFilter(Filter):
    title: enums.DignityTitle | None

    # order_by: list[str] = ['title']

    class Constants(Filter.Constants):
        model = models.Dignity
