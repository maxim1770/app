from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums


class FundFilter(Filter):
    title: enums.FundTitle | None = None
    library: enums.LibraryTitle | None = None

    class Constants(Filter.Constants):
        model = models.Fund
