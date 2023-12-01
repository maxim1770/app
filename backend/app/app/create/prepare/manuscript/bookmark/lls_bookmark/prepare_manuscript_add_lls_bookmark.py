from app import schemas, enums
from .lls_bookmark import LlsBookFullType
from ..prepare_manuscript_bookmark import get_bookmark_data_in


def prepare_manuscript_add_lls_bookmark(
        add_lls_bookmarks_data: LlsBookFullType,
        *,
        not_numbered_pages: str,
        has_left_and_right: bool,
        first_page_position: enums.PagePosition | None = None
) -> list[schemas.BookmarkDataCreate]:
    bookmarks_data_in: list[schemas.BookmarkDataCreate] = []
    not_numbered_pages = schemas.SortedNotNumberedPages()
    lls_bookmarks_data_list = [
        (lls_bookmark_data[0], lls_bookmark_data[1] + 1, lls_bookmark_data[2] + 1)
        for lls_bookmark_data in add_lls_bookmarks_data[0]
    ] if add_lls_bookmarks_data[1] == 3 else add_lls_bookmarks_data[0]
    for i, add_lls_bookmark_data in enumerate(lls_bookmarks_data_list):
        first_page_num: int = add_lls_bookmark_data[1] - add_lls_bookmarks_data[1]
        end_page_num: int = add_lls_bookmark_data[2] - add_lls_bookmarks_data[1]
        bookmarks_data_in.append(
            get_bookmark_data_in(
                first_page_num,
                end_page_num=end_page_num,
                not_numbered_pages=not_numbered_pages,
                has_left_and_right=has_left_and_right,
                first_page_position=first_page_position,
                book_data_in=add_lls_bookmark_data[0],
                bookmark_in=schemas.BookmarkCreate()
            )
        )
    return bookmarks_data_in
