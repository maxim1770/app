from app import schemas, enums
from .__book_data_create_factory import MolitvaBookDataCreateFactory, HolidayBookDataCreateFactory, \
    TopicBookDataCreateFactory, MovableDateBookDataCreateFactory, ZachaloBookDataGetFactory
from ....const import BookRegex


class BookDataCreateFactoryFactory(object):

    @classmethod
    def get(
            cls,
            bookmark_title: str,
            *,
            main_author: str | None,
            book_title: enums.BookTitle | None,
            book_type: enums.BookType | None
    ) -> schemas.BookDataType | None:
        bookmark_title = bookmark_title.replace('Глава ', '').strip()

        if bookmark_title.isdigit() or '?' in bookmark_title:
            return None

        if bookmark_title.split()[0].isdigit():
            bookmark_title: str = ' '.join(bookmark_title.split()[1:])

        if book_type and not any(book_type_ in bookmark_title for book_type_ in enums.BookType):
            bookmark_title = f'{bookmark_title} {book_type}'

        if BookRegex.MOLITVA.match(bookmark_title):
            book_data_create_factory_cls = MolitvaBookDataCreateFactory
        elif BookRegex.TOPIC.match(bookmark_title):
            book_data_create_factory_cls = TopicBookDataCreateFactory
        elif BookRegex.HOLIDAY.match(bookmark_title):
            book_data_create_factory_cls = HolidayBookDataCreateFactory
        elif 'Нд' in bookmark_title or any(day in bookmark_title for day in enums.MovableDayStrastnajaSedmitsaRu):
            book_data_create_factory_cls = MovableDateBookDataCreateFactory
        else:
            return None

        book_data_in: schemas.BookDataType = book_data_create_factory_cls(bookmark_title).book_data_in

        if book_data_in.book_data_in.saint_slug is None:
            book_data_in.book_data_in.saint_slug = main_author
        if book_data_in.book_data_in.book_in.title is None:
            book_data_in.book_data_in.book_in.title = book_title

        return book_data_in


class BookDataGetFactoryFactory(object):

    @classmethod
    def get(
            cls,
            bookmark_title: str,
            *,
            head_bookmark_title: str,
            book_title: enums.BookTitle,
    ) -> schemas.BookDataGetType | None:
        bookmark_title = bookmark_title.replace('Глава ', '').strip()

        if bookmark_title.isdigit() or '?' in bookmark_title:
            return None

        if bookmark_title.split()[0].isdigit():
            bookmark_title: str = ' '.join(bookmark_title.split()[1:])

        if bookmark_title.startswith('Зачало'):
            book_data_get_factory_cls = ZachaloBookDataGetFactory
        else:
            return None

        book_data_get: schemas.BookDataGetType = book_data_get_factory_cls(
            bookmark_title,
            head_bookmark_title=head_bookmark_title,
            book_title=book_title
        ).book_data_get

        return book_data_get
