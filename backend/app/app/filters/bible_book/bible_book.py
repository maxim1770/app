from fastapi_filter.contrib.sqlalchemy import Filter

from app import models


class BibleBookFilter(Filter):
    class Constants(Filter.Constants):
        model = models.BibleBook
