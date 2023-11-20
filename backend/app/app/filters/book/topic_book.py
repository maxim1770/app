from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums
from .topic import TopicFilter


class TopicBookFilter(Filter):
    source: enums.BookSource | None = None

    topics: TopicFilter | None = FilterDepends(with_prefix('topics', TopicFilter))

    class Constants(Filter.Constants):
        model = models.TopicBook
