from typing import Final

from pypdf import PdfReader
from pypdf.types import OutlineType

from app.schemas import PdfBookmark, FitSchema

__BASE_BOOKMARK_TITLE: Final[str] = 'BASE_BOOKMARK_TITLE'


def __get_bookmarks(
        reader: PdfReader,
        outline: OutlineType,
        *,
        parent_bookmark: PdfBookmark
) -> list[PdfBookmark]:
    for destination in outline:
        if isinstance(destination, list):
            __get_bookmarks(reader, destination, parent_bookmark=parent_bookmark.children[-1])
        else:
            page_index: int = reader.get_destination_page_number(destination)
            page_label: int = int(reader.page_labels[page_index])
            parent: PdfBookmark | None = parent_bookmark if parent_bookmark.title != __BASE_BOOKMARK_TITLE else None
            fit: FitSchema | None = FitSchema(left=destination.left, top=destination.top,
                                              zoom=destination.zoom) \
                if destination.left is not None else None
            bookmark = PdfBookmark(page_num=page_label, title=destination.title, fit=fit, parent=parent)
            parent_bookmark.children.append(bookmark)
    bookmarks: list[PdfBookmark] = parent_bookmark.children
    return bookmarks


def get_bookmarks(reader: PdfReader) -> list[PdfBookmark]:
    parent_bookmark = PdfBookmark(page_num=1, title=__BASE_BOOKMARK_TITLE)
    return __get_bookmarks(reader, reader.outline, parent_bookmark=parent_bookmark)
