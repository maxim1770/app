import io
import logging
from pathlib import Path
from typing import Any

from pydantic.color import ColorTuple
from pypdf import PdfReader, PdfWriter
from pypdf.generic import IndirectObject, Fit, PAGE_FIT
from pypdf.types import PagemodeType

from app import utils
from app.core.config import settings
from app.schemas import PdfBookmark, FitSchema
from .__get_bookmarks import get_bookmarks


def _print_bookmarks(bookmark: PdfBookmark, *, num_space: int = 1) -> None:
    logging.info(' ' * num_space + f'{bookmark.title}, page_num={bookmark.page_num}')
    for sub_bookmark in bookmark.children:
        _print_bookmarks(sub_bookmark, num_space=num_space * 2)


def print_bookmarks(bookmarks: list[PdfBookmark]) -> None:
    for bookmark in bookmarks:
        _print_bookmarks(bookmark)


def reader2writer(reader: PdfReader) -> PdfWriter:
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    return writer


def reader2writer_with_copy_bookmarks(reader: PdfReader) -> PdfWriter:
    writer = PdfWriter()
    writer.clone_reader_document_root(reader)
    return writer


def set_show_bookmarks_panel(writer: PdfWriter) -> None:
    page_mode: PagemodeType = '/UseOutlines'
    writer.page_mode = page_mode


def upload_pdf(
        writer: PdfWriter,
        *,
        path: Path,
        object_storage: utils.ObjectStorage
) -> None:
    path: Path = Path(settings.DATA_DIR) / path
    with path.open(mode='wb') as file_:
        writer.write(file_)

    # __temp_file_path = Path('some_pdf.pdf')
    # with __temp_file_path.open(mode='wb') as file_:
    #     writer.write(file_)
    # object_storage.upload(
    #     file_path=__temp_file_path,
    #     object_path=path,
    #     object_storage_class=enums.ObjectStorageClass.STANDARD_IA
    # )
    # __temp_file_path.unlink()


def get_fit(fit_schema: FitSchema | None = None) -> Fit:
    fit = Fit.xyz(fit_schema.left, top=fit_schema.top, zoom=fit_schema.zoom) if fit_schema else PAGE_FIT
    return fit


def add_outline_item(
        writer: PdfWriter,
        *,
        bookmark: PdfBookmark,
        parent: IndirectObject | None = None
) -> IndirectObject:
    fit: Fit = get_fit(bookmark.fit)
    color: ColorTuple | None = tuple((i / 255. for i in bookmark.color.as_rgb_tuple())) if bookmark.color else None
    indirect: IndirectObject = writer.add_outline_item(
        title=bookmark.title,
        page_number=bookmark.page_num - 1,
        parent=parent,
        color=color,
        fit=fit
    )
    return indirect


def _add_bookmarks(
        writer: PdfWriter,
        *,
        bookmark: PdfBookmark,
        parent_indirect: IndirectObject | None = None
) -> None:
    indirect: IndirectObject = add_outline_item(writer, bookmark=bookmark, parent=parent_indirect)
    for sub_bookmark in bookmark.children:
        _add_bookmarks(
            writer,
            bookmark=sub_bookmark,
            parent_indirect=indirect
        )


def add_bookmarks(writer: PdfWriter, *, bookmarks: list[PdfBookmark]) -> None:
    for bookmark in bookmarks:
        _add_bookmarks(writer, bookmark=bookmark)


def _offset_pages_bookmarks(bookmark: PdfBookmark, *, num_offset_pages: int) -> None:
    bookmark.page_num = bookmark.page_num + num_offset_pages
    for sub_bookmark in bookmark.children:
        _offset_pages_bookmarks(sub_bookmark, num_offset_pages=num_offset_pages)


def offset_pages_bookmarks(bookmarks: list[PdfBookmark], *, num_offset_pages: int) -> None:
    for bookmark in bookmarks:
        _offset_pages_bookmarks(bookmark, num_offset_pages=num_offset_pages)


def get_pdf_bookmarks(
        path: Path,
        *,
        object_storage: utils.ObjectStorage
) -> list[PdfBookmark]:
    reader: PdfReader = __get_pdf_reader(path, object_storage=object_storage)
    bookmarks: list[PdfBookmark] = get_bookmarks(reader)
    return bookmarks


def get_pdf_writer(
        path: Path,
        *,
        object_storage: utils.ObjectStorage
) -> PdfWriter:
    reader: PdfReader = __get_pdf_reader(path, object_storage=object_storage)
    writer: PdfWriter = reader2writer(reader)
    return writer


def __get_pdf_reader(
        path: Path,
        *,
        object_storage: utils.ObjectStorage
) -> PdfReader:
    reader = PdfReader(Path(settings.DATA_DIR) / path)
    return reader

    object_: dict[str, Any] = object_storage.get(path)
    with io.BytesIO(object_['Body'].read()) as open_pdf_file:
        reader = PdfReader(open_pdf_file)
        return reader
