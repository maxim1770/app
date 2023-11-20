from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums


class FaceSanctityFilter(Filter):
    title: enums.FaceSanctityTitle | None = None

    class Constants(Filter.Constants):
        model = models.FaceSanctity
