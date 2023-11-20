from app import schemas, enums, utils
from .__book_data_create_factory import MolitvaBookDataCreateFactory, HolidayBookDataCreateFactory, \
    TopicBookDataCreateFactory, MovableDateBookDataCreateFactory, ZachaloBookDataGetFactory, PsaltyrBookDataGetFactory, \
    CathedralBookDataGetFactory, SomeBookDataCreateFactory
from ....const import BookRegex


class BookDataCreateFactoryFactory(object):

    @classmethod
    def get(
            cls,
            bookmark_title: str,
            *,
            main_author: str | None,
            book_title: enums.BookTitle | None,
            book_type: enums.BookType | None,
    ) -> tuple[schemas.BookDataType | None, schemas.BookmarkCreate]:
        bookmark_title: str = utils.clean_extra_spaces(bookmark_title.replace('Глава', ''))

        if len(bookmark_title) == 0:
            return None, schemas.BookmarkCreate()

        if (__chapter_num := bookmark_title).isdigit():
            return None, schemas.BookmarkCreate(chapter_num=int(__chapter_num))

        if (__chapter_num := bookmark_title.split()[0]).isdigit():
            chapter_num: int | None = int(__chapter_num)
            bookmark_title: str = ' '.join(bookmark_title.split()[1:])
        else:
            chapter_num = None

        if book_type and not any(book_type_ in bookmark_title for book_type_ in enums.BookType):
            bookmark_title = f'{bookmark_title} {book_type}'

        if '?' in bookmark_title:
            book_data_create_factory_cls = SomeBookDataCreateFactory
        elif BookRegex.MOLITVA.match(bookmark_title):
            book_data_create_factory_cls = MolitvaBookDataCreateFactory
        elif BookRegex.TOPIC.match(bookmark_title):
            book_data_create_factory_cls = TopicBookDataCreateFactory
        elif BookRegex.HOLIDAY.match(bookmark_title):
            book_data_create_factory_cls = HolidayBookDataCreateFactory
        elif 'Нд' in bookmark_title or any(day in bookmark_title for day in enums.MovableDayStrastnajaSedmitsaRu):
            book_data_create_factory_cls = MovableDateBookDataCreateFactory
        else:
            book_data_create_factory_cls = SomeBookDataCreateFactory

        book_data_in: schemas.BookDataType = book_data_create_factory_cls(bookmark_title).book_data_in

        if book_data_in.book_data_in.saint_slug is None:
            book_data_in.book_data_in.saint_slug = main_author
        if book_data_in.book_data_in.book_in.title is None:
            book_data_in.book_data_in.book_in.title = book_title

        bookmark_in = schemas.BookmarkCreate(chapter_num=chapter_num)

        return book_data_in, bookmark_in


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

        if bookmark_title.startswith(enums.BookType.Zachalo):
            book_data_get_factory_cls = ZachaloBookDataGetFactory
        elif bookmark_title.startswith(enums.BookType.Psalom):
            book_data_get_factory_cls = PsaltyrBookDataGetFactory
        elif bookmark_title.startswith(enums.BookType.Pravilo):
            book_data_get_factory_cls = CathedralBookDataGetFactory
        else:
            return None
        book_data_get: schemas.BookDataGetType = book_data_get_factory_cls(
            bookmark_title,
            head_bookmark_title=head_bookmark_title,
            book_title=book_title
        ).book_data_get
        return book_data_get
