from __future__ import annotations

from pydantic import BaseModel
from pypdf import PdfReader
from pypdf.generic import Destination


class PdfBookmark(BaseModel):
    title: str
    page: int
    children: list[PdfBookmark] = []


def convert_bookmark_to_schemas(
        reader: PdfReader,
        bookmark_list: list[Destination | list[Destination]],
        *,
        parent: PdfBookmark = PdfBookmark(page=0, title='base')
) -> list[PdfBookmark]:
    for item in bookmark_list:
        if isinstance(item, list):
            convert_bookmark_to_schemas(reader, item, parent=parent.children[-1])
        else:
            page_index: int = reader.get_destination_page_number(item)
            page_label: int = int(reader.page_labels[page_index])
            pdf_bookmark = PdfBookmark(page=page_label, title=item.title)
            parent.children.append(pdf_bookmark)
    bookmarks: list[PdfBookmark] = parent.children
    return bookmarks
