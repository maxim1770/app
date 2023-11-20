from app import schemas, enums, const
from .lls_bookmark import LlsBookFullType, clean_lls_bookmark_title, LlsBookTitleType
from ..prepare_manuscript_bookmark import get_bookmark_data_in


def prepare_manuscript_lls_bookmark(
        lls_bookmarks_data: LlsBookFullType,
        *,
        not_numbered_pages: str,
        has_left_and_right: bool,
        first_page_position: enums.PagePosition | None = None
) -> list[schemas.BookmarkDataCreate]:
    bookmarks_data_in: list[schemas.BookmarkDataCreate] = []
    # not_numbered_pages = schemas.SortedNotNumberedPages.model_validate(not_numbered_pages)
    not_numbered_pages = schemas.SortedNotNumberedPages()
    lls_bookmarks_data_list = [
        (*lls_bookmark_data[:-1], lls_bookmark_data[-1] + 1) for lls_bookmark_data in lls_bookmarks_data[0]
    ] if lls_bookmarks_data[1] == 3 else lls_bookmarks_data[0]
    for i, lls_bookmark_data in enumerate(lls_bookmarks_data_list):
        if lls_bookmark_data[0] and isinstance(lls_bookmark_data[0], str) and '-' == lls_bookmark_data[0].strip():
            continue
        __bookmark_title: LlsBookTitleType = lls_bookmark_data[-2]
        if isinstance(__bookmark_title, int):
            year_title_int: int = __bookmark_title + const.NUM_OFFSET_YEARS
            bookmark_title = None
            has_year_at_start = True
        elif isinstance(__bookmark_title, str):
            bookmark_title: str = clean_lls_bookmark_title(__bookmark_title)
            year_title_int = None
            has_year_at_start = False
        elif isinstance(__bookmark_title, tuple):
            if isinstance(__bookmark_title[0], int):
                offset_year_title_int, bookmark_title = __bookmark_title
                year_title_int: int = offset_year_title_int + const.NUM_OFFSET_YEARS
                bookmark_title: str = clean_lls_bookmark_title(bookmark_title)
                has_year_at_start = True
            else:
                bookmark_title, offset_year_title_int = __bookmark_title
                year_title_int: int = offset_year_title_int + const.NUM_OFFSET_YEARS
                bookmark_title: str = clean_lls_bookmark_title(bookmark_title)
                has_year_at_start = False
        lls_book_data_in = schemas.LlsBookDataCreate(
            book_data_in=schemas.BookDataCreate(
                book_in=schemas.BookCreate(
                    title=enums.BookTitle.Lls,
                    bookmark_title=bookmark_title if bookmark_title else None,
                ),
            ),
            lls_book_in=schemas.LlsBookCreate(
                is_chapter=False if len(lls_bookmark_data) == 3 else True,
                has_year_at_start=has_year_at_start
            ),
            year_in=schemas.YearCreate(title=str(year_title_int)) if year_title_int else None
        )
        first_page_num: int = lls_bookmark_data[-1]
        if i + 1 < len(lls_bookmarks_data_list):
            end_page_num: int = lls_bookmarks_data_list[i + 1][-1]
        bookmarks_data_in.append(
            get_bookmark_data_in(
                first_page_num,
                end_page_num=end_page_num,
                not_numbered_pages=not_numbered_pages,
                has_left_and_right=has_left_and_right,
                first_page_position=first_page_position,
                book_data_in=lls_book_data_in,
                bookmark_in=schemas.BookmarkCreate()
            )
        )
    return bookmarks_data_in
