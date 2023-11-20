from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums


class TipikonFilter(Filter):
    title: enums.TipikonTitle | None = None

    # order_by: list[str] = ['priority']

    class Constants(Filter.Constants):
        model = models.Tipikon
