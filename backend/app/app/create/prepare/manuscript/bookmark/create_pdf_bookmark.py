import logging
from pathlib import Path

import boto3
from pypdf import PdfWriter
from sqlalchemy.orm import Session

from app import utils, models, crud, schemas
from .common import get_pdf_writer, add_bookmarks, upload_pdf, set_show_bookmarks_panel
from .kormchaya_bookmark import kormchaya_bookmark_data, get_kormchaya_bookmarks
from .lls_bookmark import lls_bookmark_data, get_lls_bookmarks
from .psaltyr_bookmark import psaltyr_bookmark_data, get_psaltyr_bookmarks


def create_psaltyr_pdf_bookmarks(db: Session, *, boto_session: boto3.session.Session) -> None:
    object_storage = utils.ObjectStorage(boto_session)
    for manuscript_code, psaltyr_book in [
        # ('f-304i-87', psaltyr_bookmark_data.f_304i_87),
        # ('f-37-216', psaltyr_bookmark_data.f_37_216),
        # ('f-173i-11', psaltyr_bookmark_data.f_173i_11),
        ('2eadd685-eb71-40c5-bdec-7e9dc9b7efce', psaltyr_bookmark_data.psaltyr_s_vossledovaniem_1),
        # ('a05ec697-47ed-4ccf-bc2c-5b8025cc8127', psaltyr_bookmark_data.psaltyr_tolkovaya_s_pribavleniyami),
        # ('44e98e44-f6a7-43bb-bd45-c56bc603e93d', psaltyr_bookmark_data.psaltyr_8)
    ]:
        bookmarks: list[schemas.PdfBookmark] = get_psaltyr_bookmarks(psaltyr_book)
        __create_pdf_bookmarks(db, object_storage=object_storage, manuscript_code=manuscript_code, bookmarks=bookmarks)


def create_kormchaya_pdf_bookmarks(db: Session, *, boto_session: boto3.session.Session) -> None:
    object_storage = utils.ObjectStorage(boto_session)
    for manuscript_code, kormchaya_book in [
        ('f-304i-206', kormchaya_bookmark_data.f_304i_206),
        ('e40b1692-8a78-4543-8495-3aa0c4e1deee', kormchaya_bookmark_data.kormchaya_3),
        ('fbcc305d-7632-44bb-8264-d18e4df174ac', kormchaya_bookmark_data.kormchaya_4),
        ('ba4b7090-357d-49b9-9d7d-35ce714b6236', kormchaya_bookmark_data.kormchaya_pisec_sava_danilov)
    ]:
        bookmarks: list[schemas.PdfBookmark] = get_kormchaya_bookmarks(kormchaya_book)
        __create_pdf_bookmarks(db, object_storage=object_storage, manuscript_code=manuscript_code, bookmarks=bookmarks)


def create_lls_pdf_bookmarks(db: Session, *, boto_session: boto3.session.Session) -> None:
    object_storage = utils.ObjectStorage(boto_session)
    for manuscript_code, lls_book in [
        ('lls-book-1', lls_bookmark_data.lls_book_1),
        ('lls-book-2', lls_bookmark_data.lls_book_2),
        ('lls-book-3', lls_bookmark_data.lls_book_3),
        ('lls-book-4', lls_bookmark_data.lls_book_4),
        ('lls-book-6', lls_bookmark_data.lls_book_6),
        ('lls-book-7', lls_bookmark_data.lls_book_7),
        ('lls-book-8', lls_bookmark_data.lls_book_8),
        ('lls-book-9', lls_bookmark_data.lls_book_9),
        ('lls-book-10', lls_bookmark_data.lls_book_10),
        ('lls-book-rus-1', lls_bookmark_data.lls_book_rus_1),
        ('lls-book-rus-2', lls_bookmark_data.lls_book_rus_2),
        ('lls-book-rus-3', lls_bookmark_data.lls_book_rus_3),
        ('lls-book-rus-4', lls_bookmark_data.lls_book_rus_4),
        ('lls-book-rus-5', lls_bookmark_data.lls_book_rus_5),
        ('lls-book-rus-6', lls_bookmark_data.lls_book_rus_6),
        ('lls-book-rus-7', lls_bookmark_data.lls_book_rus_7),
        ('lls-book-rus-8', lls_bookmark_data.lls_book_rus_8),
        ('lls-book-rus-9', lls_bookmark_data.lls_book_rus_9),
        ('lls-book-rus-10', lls_bookmark_data.lls_book_rus_10),
        ('lls-book-rus-11', lls_bookmark_data.lls_book_rus_11),
        ('lls-book-rus-12', lls_bookmark_data.lls_book_rus_12),
        ('lls-book-rus-13', lls_bookmark_data.lls_book_rus_13),
        ('lls-book-rus-14', lls_bookmark_data.lls_book_rus_14),
        ('lls-book-rus-15', lls_bookmark_data.lls_book_rus_15),
        ('lls-book-rus-16', lls_bookmark_data.lls_book_rus_16),
        ('lls-book-rus-17', lls_bookmark_data.lls_book_rus_17),
        ('lls-book-rus-18', lls_bookmark_data.lls_book_rus_18),
        ('lls-book-rus-19', lls_bookmark_data.lls_book_rus_19),
        ('lls-book-rus-20', lls_bookmark_data.lls_book_rus_20),
        ('lls-book-rus-21', lls_bookmark_data.lls_book_rus_21),
        ('lls-book-rus-22', lls_bookmark_data.lls_book_rus_22),
        ('lls-book-rus-23', lls_bookmark_data.lls_book_rus_23),
    ]:
        bookmarks: list[schemas.PdfBookmark] = get_lls_bookmarks(lls_book)
        __create_pdf_bookmarks(db, object_storage=object_storage, manuscript_code=manuscript_code, bookmarks=bookmarks)


def __create_pdf_bookmarks(
        db: Session,
        *,
        object_storage: utils.ObjectStorage,
        manuscript_code: str,
        bookmarks: list[schemas.PdfBookmark]
) -> None:
    manuscript: models.Manuscript = crud.manuscript.get_by_code(db, code=manuscript_code)
    manuscript_pdf_path: Path = utils.assemble_manuscript_pdf_path(manuscript, object_storage=object_storage)
    writer: PdfWriter = get_pdf_writer(manuscript_pdf_path, object_storage=object_storage)
    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    upload_pdf(writer, path=manuscript_pdf_path, object_storage=object_storage)
    logging.info(manuscript_pdf_path)
