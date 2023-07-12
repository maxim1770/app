import logging
from pathlib import Path
from subprocess import Popen, PIPE

import sqlalchemy as sa
from pypdf import PdfWriter

from app import enums, utils, models
from app.api import deps
from app.create.prepare.manuscript.bookmark.common import get_pdf_bookmarks, get_pdf_writer, offset_pages_bookmarks, \
    set_show_bookmarks_panel, save_pdf, add_bookmarks
from app.create.prepare.manuscript.bookmark.__get_bookmarks import PdfBookmark
from app.enums import PagePosition
from app.schemas import NotNumberedPages, NotNumberedPage, PageCreate

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def __prepare_zachalo_bookmark_title(bookmark_title: str) -> str:
    bookmark_title = utils.clean_extra_spaces(bookmark_title).replace('зачала', 'зачало').replace('зачало', 'Зачало')
    if '(' in bookmark_title:
        zachalo_num = int(bookmark_title.split('(', 1)[1].split(')')[0])
        bookmark_title = f'Зачало {zachalo_num}'
    # elif 'нд' in bookmark_title or 'cб' in bookmark_title:
    elif bookmark_title.split(',')[0].split()[1].isdigit() and \
            len(bookmark_title.split(',')[0].split()) == 2:
        bookmark_title = bookmark_title.split(',')[0].strip()
    return bookmark_title


def prepare_f_178i_9500():
    def __add_head_bookmark(bookmarks: list[PdfBookmark]) -> list[PdfBookmark]:
        head_bookmark = PdfBookmark(title=enums.BibleBookAbbr.Jn.name, page_num=bookmarks[0].page_num)
        dash_bookmark_index: int | None = next(
            (i for i, bookmark in enumerate(bookmarks) if '-' == bookmark.title), None)
        head_bookmark_children, bookmarks = bookmarks[:dash_bookmark_index + 1], bookmarks[dash_bookmark_index + 1:]
        head_bookmark.children = head_bookmark_children
        bookmarks = [head_bookmark] + bookmarks
        return bookmarks

    pdf_path = Path(r"C:\Users\MaxDroN\python_projects\data\pdf\manuscripts\rsl\f_178i\f-178i-9500_backup.pdf")
    pdf_path_part_1 = Path(r"C:\Users\MaxDroN\pravoslavie\bibliya\novyj_zavet\evangel\f-178i-9500_part_1_backup.pdf")
    pdf_path_part_2 = Path(r"C:\Users\MaxDroN\pravoslavie\bibliya\novyj_zavet\evangel\f-178i-9500_part_2_backup.pdf")
    out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-178i-9500 — копия_.pdf')
    writer: PdfWriter = get_pdf_writer(pdf_path)

    bookmarks = get_pdf_bookmarks(pdf_path)
    bookmarks: list[PdfBookmark] = __add_head_bookmark(bookmarks)

    bookmarks_part_1 = get_pdf_bookmarks(pdf_path_part_1)
    bookmarks_part_2 = get_pdf_bookmarks(pdf_path_part_2)

    bookmarks_part_1 = [bookmark for bookmark in bookmarks_part_1 if '|зачало|' in bookmark.title]
    bookmarks_part_1[0].title = enums.BibleBookAbbr.Mt.name
    bookmarks_part_1[1].title = enums.BibleBookAbbr.Mk.name
    bookmarks_part_1[2].title = enums.BibleBookAbbr.Lk.name
    bookmarks_part_2 = [bookmark for bookmark in bookmarks_part_2 if '|зачало|' in bookmark.title]
    bookmarks_part_2[0].title = enums.BibleBookAbbr.Lk.name

    offset_pages_bookmarks(bookmarks_part_1, num_offset_pages=6)
    offset_pages_bookmarks(bookmarks_part_2, num_offset_pages=6 + 316)

    bookmarks_part_1[2].children = bookmarks_part_1[2].children + bookmarks_part_2[0].children

    for head_bookmark in bookmarks_part_1 + bookmarks[:1]:
        for bookmark in head_bookmark.children:
            if 'зач' in bookmark.title.lower():
                bookmark.title = __prepare_zachalo_bookmark_title(bookmark.title)

    bookmarks = bookmarks_part_1 + bookmarks

    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def prepare_f_256_472():
    pdf_path = Path(r"C:\Users\MaxDroN\python_projects\data\pdf\manuscripts\rsl\f_256\f-256-472_backup.pdf")
    pdf_path_part_1 = Path(
        r"C:\Users\MaxDroN\pravoslavie\bibliya\novyj_zavet\evangel\tolkovoye\f-256-472_part_1_backup.pdf")
    out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-256-472 — merge.pdf')
    writer: PdfWriter = get_pdf_writer(pdf_path)

    bookmarks = get_pdf_bookmarks(pdf_path)

    bookmarks_part_1 = get_pdf_bookmarks(pdf_path_part_1)

    bookmarks_part_1 = [bookmark for bookmark in bookmarks_part_1 if '|зачало|' in bookmark.title]
    bookmarks_part_1[0].title = enums.BibleBookAbbr.Lk.name

    bookmarks_part_1[0].fit = None
    for bookmark in bookmarks_part_1[0].children:
        bookmark.fit = None
        for bookmark_ in bookmark.children:
            bookmark_.fit = None

    offset_pages_bookmarks(bookmarks_part_1, num_offset_pages=4)

    for head_bookmark in bookmarks_part_1:
        for bookmark in head_bookmark.children:
            if 'зач' in bookmark.title.lower():
                bookmark.title = __prepare_zachalo_bookmark_title(bookmark.title)

    bookmarks = bookmarks_part_1 + bookmarks

    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def prepare_f_228_67():
    pdf_path = Path(r"C:\Users\MaxDroN\pravoslavie\bibliya\novyj_zavet\evangel\tolkovoye\f-228-67_backup.pdf")
    out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-228-67 — prepare.pdf')
    writer: PdfWriter = get_pdf_writer(pdf_path)

    bookmarks = get_pdf_bookmarks(pdf_path)

    bookmarks = [bookmark for bookmark in bookmarks if '|зачало|' in bookmark.title]
    bookmarks[0].title = enums.BibleBookAbbr.Mt.name
    bookmarks[1].title = enums.BibleBookAbbr.Mk.name

    for head_bookmark in bookmarks:
        for bookmark in head_bookmark.children:
            if 'зач' in bookmark.title.lower():
                bookmark.title = __prepare_zachalo_bookmark_title(bookmark.title)

    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def prepare_f_173i_5():
    pdf_path = Path(r"C:\Users\MaxDroN\pravoslavie\bibliya\novyj_zavet\apostol\f_173i_5_backup.pdf")
    # out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-173i-5 — prepare.pdf')
    out_pdf_path = Path(r"C:\Users\MaxDroN\python_projects\data\pdf\manuscripts\rsl\f_173i\f-173i-5.pdf")
    writer: PdfWriter = get_pdf_writer(out_pdf_path)

    bookmarks = get_pdf_bookmarks(pdf_path)

    bookmarks_ = []
    for bookmark in bookmarks:
        if not any(bookmark_title in bookmark.title for bookmark_title in [
            'Сказание', 'Содержание', 'епистол'
        ]):
            bookmarks_.append(bookmark)

    for bookmark, bible_book_abbr in zip(bookmarks_, list(enums.BibleBookAbbr)[4:-1]):
        bookmark.title = bible_book_abbr.name

    offset_pages_bookmarks(bookmarks, num_offset_pages=1)

    for head_bookmark in bookmarks:
        for bookmark in head_bookmark.children:
            if 'зач' in bookmark.title.lower():
                bookmark.title = __prepare_zachalo_bookmark_title(bookmark.title)

    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


def prepare_f_98_30():
    pdf_path = Path(r"C:\Users\MaxDroN\pravoslavie\bibliya\novyj_zavet\apostol\tolkovyy\f_98_30_backup.pdf")
    out_pdf_path = Path(r'C:\Users\MaxDroN\Desktop\program\m\f-98-30 — prepare.pdf')
    writer: PdfWriter = get_pdf_writer(pdf_path)

    bookmarks = get_pdf_bookmarks(pdf_path)

    bookmarks_ = []
    for bookmark in bookmarks:
        if not any(bookmark_title in bookmark.title for bookmark_title in [
            'Сказание', 'Содержание', 'епистол', 'Главы', 'Слово'
        ]):
            bookmarks_.append(bookmark)

    for bookmark, bible_book_abbr in zip(bookmarks_, list(enums.BibleBookAbbr)[4:-1]):
        bookmark.title = bible_book_abbr.name

    for head_bookmark in bookmarks:
        for bookmark in head_bookmark.children:
            if 'зач' in bookmark.title.lower():
                bookmark.title = __prepare_zachalo_bookmark_title(bookmark.title)

    add_bookmarks(writer, bookmarks=bookmarks)
    set_show_bookmarks_panel(writer)
    save_pdf(writer, path=out_pdf_path)


if __name__ == '__main__':
    # db = next(deps.get_db())


    # select = sa.select(models.Book).outerjoin(models.TopicBook).filter(
    #     models.TopicBook.id == 15001
    # )
    # a = db.execute(select).scalar_one_or_none()
    # logging.info(type(a.topic_book.topics))
    # logging.info(a.topic_book.topics[0])
    # logging.info(type(a.topic_book.topics[0]))
    # logging.info(a.topic_book.topics.__dict__)

    # select = sa.select(models.Book).outerjoin(models.TopicBook).filter(
    #     models.TopicBook.topics.astext.cast(ARRAY) == ["\u043e \u041c\u043e\u043b\u0447\u0430\u043d\u0438\u0438"]
    # )
    # a = db.execute(select).scalar_one_or_none()
    # logging.info(a)

    # create.create_all_movable_dates(db)
    # create.create_all_zachalos_movable_dates_associations(db)
    # create.create_dates_for_years(db)

    a = [line.decode('cp866', 'ignore') for line in Popen('tasklist', stdout=PIPE).stdout.readlines()]
    for i in [i_ for i_ in a if 'python.exe' in i_]:
        print(f'taskkill /F /IM {i.split()[1]}')

    # 'taskkill /F /IM {}'

    # В Windows PowerShell
    # taskkill /F /IM 12064

    # prepare_f_173i_5()
    # prepare_f_98_30()

    # logging.info(__prepare_zachalo_bookmark_title('зачало в(2)'))
    # logging.info(__prepare_zachalo_bookmark_title('Зачало 44 В Святой и Великий Четверг, Евангелие 1, на Умывении'))

    pass

    a = {'священномученику Макарию, митрополиту Киевскому', 'священномученику Мефодию, епископу Патарскому'}
    b = ' и '.join(a)
    print(b)

    some_2_not_numbered_pages = NotNumberedPages(
        [
            NotNumberedPage(
                page=PageCreate(
                    num=1,
                    position=PagePosition.right
                ),
                count=2,
            ),
            NotNumberedPage(
                page=PageCreate(
                    num=5,
                    position=PagePosition.left
                ),
                count=1,
            )
        ]
    )
    print(some_2_not_numbered_pages)