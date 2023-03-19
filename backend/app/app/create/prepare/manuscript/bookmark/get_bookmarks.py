from __future__ import annotations

from typing import Final

from pydantic import BaseModel, validator, conint, constr
from pydantic.color import Color
from pypdf import PdfReader
from pypdf.types import OutlineType


class FitSchema(BaseModel):
    left: float
    top: float
    zoom: float

    @validator('zoom')
    def round_zoom(cls, zoom: float):
        return round(zoom, 3)


class BookmarkBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=620)
    page_num: conint(strict=True, ge=1, le=1500)
    color: Color | None = None


class Bookmark(BookmarkBase):
    fit: FitSchema | None = None
    children: list[Bookmark] = []
    parent: Bookmark | None = None


class LlsBookmarkBase(BookmarkBase):
    start_on_new_page: bool


__BASE_BOOKMARK_TITLE: Final[str] = 'BASE_BOOKMARK_TITLE'


def _get_bookmarks(
        reader: PdfReader,
        outline: OutlineType,
        *,
        parent_bookmark: Bookmark
) -> list[Bookmark]:
    for destination in outline:
        if isinstance(destination, list):
            _get_bookmarks(reader, destination, parent_bookmark=parent_bookmark.children[-1])
        else:
            page_index: int = reader.get_destination_page_number(destination)
            page_label: int = int(reader.page_labels[page_index])
            fit = FitSchema(left=destination.left, top=destination.top, zoom=destination.zoom)
            parent: Bookmark | None = parent_bookmark if parent_bookmark.title != __BASE_BOOKMARK_TITLE else None
            bookmark = Bookmark(page_num=page_label, title=destination.title, fit=fit, parent=parent)
            parent_bookmark.children.append(bookmark)
    bookmarks: list[Bookmark] = parent_bookmark.children
    return bookmarks


def get_bookmarks(reader: PdfReader) -> list[Bookmark]:
    parent_bookmark = Bookmark(page_num=1, title=__BASE_BOOKMARK_TITLE)
    return _get_bookmarks(reader, reader.outline, parent_bookmark=parent_bookmark)
