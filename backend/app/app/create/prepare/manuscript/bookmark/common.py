import logging
from pathlib import Path

from pydantic.color import ColorTuple
from pypdf import PdfReader, PdfWriter
from pypdf.generic import IndirectObject, Fit, PAGE_FIT
from pypdf.types import PagemodeType

from .get_bookmarks import Bookmark, FitSchema, get_bookmarks


def _print_bookmarks(bookmark: Bookmark, *, num_space: int = 1) -> None:
    logging.info(' ' * num_space + f'{bookmark.title}, page_num={bookmark.page_num}')
    for sub_bookmark in bookmark.children:
        _print_bookmarks(sub_bookmark, num_space=num_space * 2)


def print_bookmarks(bookmarks: list[Bookmark]) -> None:
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


def save_pdf(writer: PdfWriter, *, path: Path) -> None:
    with path.open(mode='wb') as file_:
        writer.write(file_)


def get_fit(fit_schema: FitSchema | None = None) -> Fit:
    fit = Fit.xyz(fit_schema.left, top=fit_schema.top, zoom=fit_schema.zoom) if fit_schema else PAGE_FIT
    return fit


def add_outline_item(
        writer: PdfWriter,
        *,
        bookmark: Bookmark,
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
        bookmark: Bookmark,
        parent_indirect: IndirectObject | None = None
) -> None:
    indirect: IndirectObject = add_outline_item(writer, bookmark=bookmark, parent=parent_indirect)
    for sub_bookmark in bookmark.children:
        _add_bookmarks(
            writer,
            bookmark=sub_bookmark,
            parent_indirect=indirect
        )


def add_bookmarks(writer: PdfWriter, *, bookmarks: list[Bookmark]) -> None:
    for bookmark in bookmarks:
        _add_bookmarks(writer, bookmark=bookmark)


def _offset_pages_bookmarks(bookmark: Bookmark, *, num_offset_pages: int) -> None:
    bookmark.page_num = bookmark.page_num + num_offset_pages
    for sub_bookmark in bookmark.children:
        _offset_pages_bookmarks(sub_bookmark, num_offset_pages=num_offset_pages)


def offset_pages_bookmarks(bookmarks: list[Bookmark], *, num_offset_pages: int) -> None:
    for bookmark in bookmarks:
        _offset_pages_bookmarks(bookmark, num_offset_pages=num_offset_pages)


def get_pdf_bookmarks(path: Path) -> list[Bookmark]:
    reader = PdfReader(path)
    bookmarks: list[Bookmark] = get_bookmarks(reader)
    return bookmarks


def get_pdf_writer(path: Path) -> PdfWriter:
    reader = PdfReader(path)
    writer: PdfWriter = reader2writer(reader)
    return writer
