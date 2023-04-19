from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums


class FundFilter(Filter):
    title: enums.FundTitle | None
    library: enums.LibraryTitle | None

    class Constants(Filter.Constants):
        model = models.Fund
