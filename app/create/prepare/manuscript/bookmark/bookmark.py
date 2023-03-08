import logging
import re
from pathlib import Path

from pypdf import PdfReader
from sqlalchemy.orm import Session

from app import crud, schemas, const, enums
from app.api import deps
from .convert_bookmark_to_schemas import convert_bookmark_to_schemas, PdfBookmark
from .prepare_page import prepare_pages_in


def _check_holiday_day(db: Session, bookmark_data_in: schemas.BookmarkDataCreate, *,
                       month: PdfBookmark,
                       day: PdfBookmark) -> None:
    holiday = crud.holiday.get_by_slug(db, slug=bookmark_data_in.book_data_in.holiday_slug)
    if holiday.day.month != int(month.title) or holiday.day.day != int(day.title):
        logging.error("ERROR")
        logging.error(bookmark_data_in)


def prepare_manuscript_bookmark(
        *,
        pdf_path: Path,
        not_numbered_pages: str,
        from_neb: bool,
        first_page_position: enums.PagePosition | None = None
) -> list[schemas.BookmarkDataCreate]:
    db: Session = next(deps.get_db())
    not_numbered_pages = schemas.NotNumberedPages.parse_obj(not_numbered_pages)
    reader = PdfReader(pdf_path)
    pdf_bookmarks: list[PdfBookmark] = convert_bookmark_to_schemas(reader, reader.outline)
    bookmarks_data_in: list[schemas.BookmarkDataCreate] = []
    for month in pdf_bookmarks:
        logging.warning(f'{month.title}, page={month.page}')
        for i, day in enumerate(month.children):
            logging.warning(f'{day.title}, page={day.page}')
            for j, pdf_book in enumerate(day.children):
                if not pdf_book.title.isdigit() and re.match(const.REGEX_SLUG, pdf_book.title):
                    logging.info(f'{pdf_book.title}, page={pdf_book.page}')
                    if j + 1 < len(day.children):
                        end_page_num: int = day.children[j + 1].page
                    elif i + 1 < len(month.children):
                        end_page_num: int = month.children[i + 1].page
                    pages_in: schemas.PagesCreate = prepare_pages_in(
                        pdf_book.page,
                        end_page_num,
                        not_numbered_pages=not_numbered_pages,
                        from_neb=from_neb,
                        first_page_position=first_page_position
                    )
                    holiday_book_data_in = schemas.HolidayBookDataCreate(
                        book_in=schemas.BookCreate(title=None),
                        holiday_slug=pdf_book.title,
                    )
                    bookmark_data_in = schemas.BookmarkDataCreate(
                        pages_in=pages_in,
                        book_data_in=holiday_book_data_in
                    )
                    _check_holiday_day(db, bookmark_data_in, month=month, day=day)
                    bookmarks_data_in.append(bookmark_data_in)
    return bookmarks_data_in
