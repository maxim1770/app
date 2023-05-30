from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums


class FaceSanctityFilter(Filter):
    title: enums.FaceSanctityTitle | None

    # order_by: list[str] = ['title']

    class Constants(Filter.Constants):
        model = models.FaceSanctity
