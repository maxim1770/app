from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums
from .topic_book import TopicBookFilter


class BookFilter(Filter):
    title: enums.BookTitle | None
    type: enums.BookType | None
    author_id__isnull: bool | None
    topic_book: TopicBookFilter | None = FilterDepends(with_prefix('topic_book', TopicBookFilter))

    order_by: list[str] = ['title', 'type', 'author_id']

    class Constants(Filter.Constants):
        model = models.Book
