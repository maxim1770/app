from __future__ import annotations

import logging

from pydantic import BaseModel
from pypdf import PdfReader
from pypdf.generic import Destination

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


class PdfBookmark(BaseModel):
    title: str
    page: int
    children: list[PdfBookmark] = []


class PdfBookmarks(BaseModel):
    __root__: list[PdfBookmark]


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


def main():
    reader = PdfReader('../../pravoslavie/lives_saints/prologs/prolog_mart_avgust_4.pdf')
    logging.error(reader.outline[0])

    bookmarks_in: list[PdfBookmark] = convert_bookmark_to_schemas(reader, reader.outline)
    for month in bookmarks_in:
        logging.error(f'{month.title}, page={month.page}')
        for day in month.children:
            logging.warning(f'{day.title}, page={day.page}')
            for book in day.children:
                logging.info(f'{book.title}, page={book.page}')


if __name__ == "__main__":
    main()
