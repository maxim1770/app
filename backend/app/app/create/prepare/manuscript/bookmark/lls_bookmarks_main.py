import logging
from pathlib import Path
from typing import Final

from pypdf import PdfReader, PdfWriter

from app.create.prepare.manuscript.bookmark.common import add_bookmarks, reader2writer, set_show_bookmarks_panel, \
    save_pdf, reader2writer_with_copy_bookmarks, offset_pages_bookmarks, print_bookmarks
from app.create.prepare.manuscript.bookmark.get_bookmarks import get_bookmarks, Bookmark
from app.create.prepare.manuscript.bookmark.lls_bookmarks import LlsBookmark, LlsBookRusFullType, get_lls_bookmarks


logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def _lls_bookmarks_main(pdf_path: Path, *, out_pdf_path: Path, lls_book_rus: LlsBookRusFullType):
    reader = PdfReader(pdf_path)
    writer: PdfWriter = reader2writer(reader)
    bookmarks: list[Bookmark] = []
    lls_bookmarks: list[LlsBookmark] = get_lls_bookmarks(lls_book_rus)
    for i, lls_bookmark in enumerate(lls_bookmarks[:-1]):
        children: list[Bookmark] = []
        if (next_lls_bookmark := lls_bookmarks[i + 1]).start_on_new_page:
            end_bookmark = Bookmark(title='-', page=next_lls_bookmark.page_num - 1)
            children.append(end_bookmark)
        bookmarks.append(
            Bookmark(
                title=lls_bookmark.title,
                page_num=lls_bookmark.page_num,
                color=lls_bookmark.color,
                children=children)
        )
    end_lls_bookmark: LlsBookmark = lls_bookmarks[-1]
    bookmarks.append(
        Bookmark(title=end_lls_bookmark.title, page_num=end_lls_bookmark.page_num, color=end_lls_bookmark.color)
    )
    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)

def _prolog_bookmarks_main(pdf_path: Path, *, out_pdf_path: Path, prolog_book: PrologBookFullType):
    reader = PdfReader(pdf_path)
    writer: PdfWriter = reader2writer(reader)
    prolog_bookmarks: list[PrologBookmark] = get_prolog_bookmarks(prolog_book)
    print_bookmarks(prolog_bookmarks)
    add_bookmarks(writer, bookmarks=prolog_bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def main5():
    pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-256-472 — копия_.pdf')
    out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-256-472 — копия_merge.pdf')
    part_1_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-256-472_part_1 — копия.pdf')
    reader = PdfReader(pdf_path)
    writer: PdfWriter = reader2writer(reader)
    part_1_reader = PdfReader(part_1_pdf_path)
    part_1_bookmarks: list[Bookmark] = get_bookmarks(part_1_reader)
    part_1_bookmarks: list[Bookmark] = part_1_bookmarks[-1:]
    num_offset_pages: Final[int] = 4
    offset_pages_bookmarks(part_1_bookmarks, num_offset_pages=num_offset_pages)
    bookmarks: list[Bookmark] = get_bookmarks(reader)
    bookmarks = part_1_bookmarks + bookmarks
    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def _test_add_root_bookmark_and_bookmarks():
    pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-256-472.pdf')
    out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-256-472 — копия_.pdf')
    reader = PdfReader(pdf_path)
    writer: PdfWriter = reader2writer(reader)
    bookmarks: list[Bookmark] = get_bookmarks(reader)
    root_bookmark = Bookmark(title='Евангелие от Иоанна', page_num=bookmarks[0].page_num)
    root_bookmark.children = bookmarks
    add_bookmarks(writer, bookmarks=[root_bookmark])
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def main6():
    pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-98-80_backup.pdf')
    out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-98-80_backup_.pdf')
    reader = PdfReader(pdf_path)
    writer: PdfWriter = reader2writer(reader)
    bookmarks: list[Bookmark] = get_bookmarks(reader)
    end_bookmark_title: str = '52 Нд 32'
    # https://stackoverflow.com/questions/9542738/python-find-in-list
    end_bookmark_i = next(
        (i for i, bookmark in enumerate(bookmarks) if end_bookmark_title in bookmark.title), None)
    bookmarks = bookmarks[:end_bookmark_i + 1]
    for bookmark in bookmarks:
        bookmark.title = f'Слово {bookmark.title}'
    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def _test_writer():
    pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-98-80_backup.pdf')
    out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-98-80_backup__.pdf')
    reader = PdfReader(pdf_path)
    writer: PdfWriter = reader2writer_with_copy_bookmarks(reader)
    # print(writer.get_outline_root())
    print(writer.find_outline_item('19 Нд 7 по Пасце'))


def lls(pdf_path: Path, *, out_pdf_path: Path) -> None:
    reader = PdfReader(pdf_path)
    out_reader = PdfReader(out_pdf_path)
    bookmarks: list[Bookmark] = get_bookmarks(reader)
    writer: PdfWriter = reader2writer(out_reader)
    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def _test_zoom():
    """На этом примере вроде все хорошо, закладки переносятся милиметр в милиметр,
    Возможно потому что тут тот же файл в out_pdf_path, а не меньше размером, как было с lls 2 Гб -> 138 Мб
    """
    pdf_path = Path(r'C:\Users\MaxDroN\pravoslavie\history\Русь\Rus_Kniga 9.pdf')
    out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\Rus_Kniga 9_.pdf')
    reader = PdfReader(pdf_path)
    bookmarks: list[Bookmark] = get_bookmarks(reader)
    writer: PdfWriter = reader2writer(reader)
    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def lls_bookmarks_main(lls_book_rus: LlsBookRusFullType, lls_book_rus_num: int) -> None:
    lls_book_rus_str: str = f'lls-book-rus-{lls_book_rus_num}'
    pdf_path = Path(f'C:/Users/MaxDroN/python_projects/data/pdf/manuscripts/lls/{lls_book_rus_str}.pdf')
    out_pdf_path = Path(f'C:/Users/MaxDroN/Desktop/program/lls/{lls_book_rus_str}_.pdf')
    _lls_bookmarks_main(pdf_path, out_pdf_path=out_pdf_path, lls_book_rus=lls_book_rus)


def prolog_bookmarks_main(prolog_book: PrologBookFullType) -> None:
    pdf_path = Path(r'C:\Users\MaxDroN\python_projects\data\pdf\manuscripts\nlr\sof\df82e287-0f6c-420b-a163-e4f03e9dfca6_old_backup.pdf')
    out_pdf_path = Path(r"C:\Users\MaxDroN\Desktop\df82e287-0f6c-420b-a163-e4f03e9dfca6_old_backup__.pdf")
    _prolog_bookmarks_main(pdf_path, out_pdf_path=out_pdf_path, prolog_book=prolog_book)


def lls_bookmarks_roman_main(lls_book: LlsBookRusFullType, lls_book_num: int) -> None:
    lls_book_str: str = f'lls-book-{lls_book_num}'
    pdf_path = Path(f'C:/Users/MaxDroN/python_projects/data/pdf/manuscripts/lls/{lls_book_str}.pdf')
    out_pdf_path = Path(f'C:/Users/MaxDroN/Desktop/program/lls/{lls_book_str}_.pdf')
    _lls_bookmarks_main(pdf_path, out_pdf_path=out_pdf_path, lls_book_rus=lls_book)


if __name__ == '__main__':
    # verify_all_lls_pages()
    prolog_bookmarks_main(velikie_minei_cheti_sentyabr)
    # lls_bookmarks_roman_main(const.lls_book_6, 6)
    # lls_bookmarks_main(const.lls_book_rus_21, 21)
    # lls_bookmarks_main(const.lls_book_rus_11, 11)

    # pdf_path = Path(r'C:\Users\MaxDroN\python_projects\data\pdf\manuscripts\lls\lls-book-rus-7__backup.pdf')
    # out_pdf_path = Path(r'C:\Users\MaxDroN\python_projects\data\pdf\manuscripts\lls\lls-book-rus-7.pdf')
    # lls(pdf_path, out_pdf_path=out_pdf_path)

    # pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-98-80_backup.pdf')
    # out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-98-80_backup___.pdf')
    # reader = PdfReader(pdf_path)
    # print(reader.pages[0])
    # print(type(reader.outline[0]))
    # print(reader.outline[0])
    # print(reader.outline[0].dest_array)
    # print(reader.outline[0].typ)
    # print(type(reader.outline[0].typ))
    #
    # for x in reader.outline[10:]:
    # print(x)
    #
    # print(reader.outline[0].left)
    # print(type(reader.outline[0].left))
    #
    # print(reader.outline[4])
    # print(reader.outline[5].dest_array)
    # writer: PdfWriter = reader2writer(reader)
    # fit: Fit = Fit.xyz(left=reader.outline[0].left, top=reader.outline[5].top, zoom=reader.outline[5].zoom)
    # print(fit.fit_args)
    # fit.fit_args = [0.0, 1586, 2.2]
    # print(fit.fit_args)
    # bookmark: IndirectObject = writer.add_outline_item(
    # title=reader.outline[5].title,
    # page_number=reader.outline[5].page,
    # fit=fit
    # )
    # save_pdf(writer, path=out_pdf_path)

    pass
