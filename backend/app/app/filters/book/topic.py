from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums


class TopicFilter(Filter):
    title__in: list[enums.BookTopic] | None = None

    class Constants(Filter.Constants):
        model = models.Topic
