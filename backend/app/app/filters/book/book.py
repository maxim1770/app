from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums
from .topic_book import TopicBookFilter


class BookFilter(Filter):
    title: enums.BookTitle | None = None
    type: enums.BookType | None = None
    topic_book: TopicBookFilter | None = FilterDepends(with_prefix('topic_book', TopicBookFilter))

    order_by: list[str] = []

    class Constants(Filter.Constants):
        model = models.Book
