from pathlib import Path

from app import schemas, enums, utils
from .__convert_page import pages_nums2pages_in
from ._book_data_create_factory_factory import BookDataCreateFactoryFactory, BookDataGetFactoryFactory
from .common import get_pdf_bookmarks


def prepare_manuscript_bookmark(
        *,
        pdf_path: Path,
        not_numbered_pages: str,
        from_neb: bool,
        first_page_position: enums.PagePosition | None = None
) -> list[schemas.BookmarkDataCreate]:
    bookmarks_data_in: list[schemas.BookmarkDataCreate] = []
    not_numbered_pages = schemas.NotNumberedPages.model_validate(not_numbered_pages)
    bookmarks: list[schemas.PdfBookmark] = get_pdf_bookmarks(pdf_path)
    try:
        book_title = enums.BookTitle._value2member_map_[bookmarks[0].title.replace('Название: ', '')]
    except KeyError:
        book_title = None
    else:
        bookmarks = bookmarks[1:]
    if 'Автор:' in bookmarks[0].title:
        main_author: str = utils.clean_extra_spaces(bookmarks[0].title.replace('Автор: ', ''))
        bookmarks = bookmarks[1:]
    else:
        main_author: str | None = None
    try:
        book_type = enums.BookType._value2member_map_[bookmarks[0].title.replace('Тип: ', '')]
    except KeyError:
        book_type = None
    else:
        bookmarks = bookmarks[1:]
    if bookmarks[0].children and bookmarks[0].children[0].title.isdigit():
        for bookmark_month in bookmarks:
            for i, bookmark_day in enumerate(bookmark_month.children):
                for j, bookmark_ in enumerate(bookmark_day.children):
                    book_data_in: schemas.BookDataType | None = BookDataCreateFactoryFactory.get(
                        bookmark_.title,
                        main_author=main_author,
                        book_title=book_title,
                        book_type=book_type
                    )
                    if book_data_in is None:
                        continue
                    first_page_num: int = bookmark_.page_num
                    if j + 1 < len(bookmark_day.children):
                        end_page_num: int = bookmark_day.children[j + 1].page_num
                    elif i + 1 < len(bookmark_month.children):
                        end_page_num: int = bookmark_month.children[i + 1].page_num
                    bookmarks_data_in.append(
                        __get_bookmark_data_in(first_page_num, end_page_num=end_page_num,
                                               not_numbered_pages=not_numbered_pages, from_neb=from_neb,
                                               first_page_position=first_page_position, book_data_in=book_data_in)
                    )
    elif bookmarks[0].children and bookmarks[0].children[0].title != '-':
        for i, head_bookmark in enumerate(bookmarks):
            for j, bookmark in enumerate(head_bookmark.children):
                book_data_in: schemas.BookDataGetType | None = BookDataGetFactoryFactory.get(
                    bookmark.title,
                    head_bookmark_title=head_bookmark.title,
                    book_title=book_title,
                )
                if book_data_in is None:
                    continue
                first_page_num: int = bookmark.page_num
                if bookmark.children and bookmark.children[0].title == '-':
                    end_page_num: int = bookmark.children[0].page_num
                elif j + 1 < len(head_bookmark.children):
                    end_page_num: int = head_bookmark.children[j + 1].page_num
                elif i + 1 < len(bookmarks):
                    end_page_num: int = bookmarks[i + 1].page_num
                bookmarks_data_in.append(
                    __get_bookmark_data_in(first_page_num, end_page_num=end_page_num,
                                           not_numbered_pages=not_numbered_pages, from_neb=from_neb,
                                           first_page_position=first_page_position, book_data_in=book_data_in)
                )
    else:
        for i, bookmark in enumerate(bookmarks):
            book_data_in: schemas.BookDataType | None = BookDataCreateFactoryFactory.get(
                bookmark.title,
                main_author=main_author,
                book_title=book_title,
                book_type=book_type
            )
            if book_data_in is None:
                continue
            first_page_num: int = bookmark.page_num
            if bookmark.children and bookmark.children[0].title == '-':
                end_page_num: int = bookmark.children[0].page_num
            elif i + 1 < len(bookmarks):
                end_page_num: int = bookmarks[i + 1].page_num
            bookmarks_data_in.append(
                __get_bookmark_data_in(first_page_num, end_page_num=end_page_num,
                                       not_numbered_pages=not_numbered_pages, from_neb=from_neb,
                                       first_page_position=first_page_position, book_data_in=book_data_in)
            )
    return bookmarks_data_in


def __get_bookmark_data_in(
        first_page_num,
        *,
        end_page_num,
        not_numbered_pages,
        from_neb,
        first_page_position,
        book_data_in
) -> schemas.BookmarkDataCreate:
    pages_in: schemas.PagesCreate = pages_nums2pages_in(
        first_page_num,
        end_page_num,
        not_numbered_pages=not_numbered_pages,
        from_neb=from_neb,
        first_page_position=first_page_position
    )
    bookmark_data_in = schemas.BookmarkDataCreate(
        pages_in=pages_in,
        book_data_in=book_data_in
    )
    return bookmark_data_in
