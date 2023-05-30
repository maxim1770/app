import logging
from pathlib import Path

from app.create.prepare.manuscript.bookmark.common import get_pdf_bookmarks
from app.create.prepare.manuscript.bookmark.get_bookmarks import Bookmark

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def __compare_bookmarks_for_prolog(bookmark: Bookmark, backup_bookmark: Bookmark) -> None:
    if bookmark.title != backup_bookmark.title:
        logging.warning(f'{bookmark.parent.parent.title}.{bookmark.parent.title}')
        if len(bookmark.title) < 3:
            logging.error(f'! ERROR !')
        if len(backup_bookmark.title) > 3:
            logging.error(f'{bookmark.title}')
            logging.error(f'{backup_bookmark.title}')
        else:
            logging.info(f'{bookmark.title}')
            logging.info(f'{backup_bookmark.title}')
        logging.warning('- - -')


def __get_bookmarks_titles(bookmarks: list[Bookmark]) -> list[str]:
    return [child.title for child in bookmarks if child.title != '-']


def __check_new(children_titles: list[str], *, backup_children_titles: list[str]) -> list[str]:
    found_titles: list[str] = []
    for child_title in set(children_titles) - set(backup_children_titles):
        found_title = child_title
        logging.warning(f'New Item {found_title}')
        found_titles.append(found_title)
    return found_titles


def __check_new_glas(children_titles: list[str], *, backup_children_titles: list[str]) -> list[str]:
    found_titles: list[str] = []

    def __remove_glas_num(bookmarks_titles: list[str]) -> list[tuple[str, int]]:
        bookmarks_titles_with_glas_nums = []
        for child_title in bookmarks_titles:
            try:
                glas_num: int = int(child_title[child_title.find('глас') + 4:].strip()[0])
            except ValueError as e:
                continue
            child_title = child_title.replace(str(glas_num), '').replace('  ', ' ')
            bookmarks_titles_with_glas_nums.append((child_title, glas_num))
        return bookmarks_titles_with_glas_nums

    def __remove_upom(bookmarks_titles: list[str]) -> list[str]:
        return [child_title for child_title in bookmarks_titles if 'Упоминание' not in child_title]

    def _prepare_foo(bookmarks_titles: list[str]) -> list[tuple[str, int]]:
        return __remove_glas_num(__remove_upom(bookmarks_titles))

    for child_title in set([i[0] for i in _prepare_foo(children_titles)]) & set(
            [i[0] for i in _prepare_foo(backup_children_titles)]):
        found_title = child_title.replace("глас ",
                                          f"глас {[i[1] for i in _prepare_foo(children_titles) if i[0] == child_title][0]} ")
        backup_found_title = child_title.replace("глас ",
                                                 f"глас {[i[1] for i in _prepare_foo(backup_children_titles) if i[0] == child_title][0]} ")
        logging.warning(f'New глас:')
        logging.info(f'New {found_title}')
        logging.info(f'Old {backup_found_title}')
        logging.warning(f'- - -')

        found_titles.append(found_title)
        found_titles.append(backup_found_title)

    return found_titles


def __check_new_slug(children_titles: list[str], *, backup_children_titles: list[str]) -> list[str]:
    found_titles: list[str] = []

    def __remove_slug(bookmarks_titles: list[str]) -> list[tuple[str, int]]:
        bookmarks_titles_with_slug = []
        for child_title in bookmarks_titles:
            slug: str = child_title[child_title.find('глас') + 4:].strip()[2:].strip()
            child_title = child_title.replace(slug, '').strip()
            bookmarks_titles_with_slug.append((child_title, slug))
        return bookmarks_titles_with_slug

    def __remove_upom(bookmarks_titles: list[str]) -> list[str]:
        return [child_title for child_title in bookmarks_titles if 'Упоминание' not in child_title]

    def _prepare_foo(bookmarks_titles: list[str]) -> list[tuple[str, int]]:
        return __remove_slug(__remove_upom(bookmarks_titles))

    for child_title in set([i[0] for i in _prepare_foo(children_titles)]) & set(
            [i[0] for i in _prepare_foo(backup_children_titles)]):
        found_title = f'{child_title} {[i[1] for i in _prepare_foo(children_titles) if i[0] == child_title][0]}'
        backup_found_title = f'{child_title} {[i[1] for i in _prepare_foo(backup_children_titles) if i[0] == child_title][0]}'

        logging.warning(f'New slug:')
        logging.info(f'New {found_title}')
        logging.info(f'Old {backup_found_title}')
        logging.warning(f'- - -')

        found_titles.append(found_title)
        found_titles.append(backup_found_title)

    return found_titles


def __remove_found_titles(children_titles: list[str], *, found_titles: list[str]) -> list[str]:
    children_titles = list(set(children_titles) - set(found_titles))
    return children_titles


def __compare_bookmarks_for_month_word(bookmark: Bookmark, backup_bookmark: Bookmark) -> None:
    if bookmark.parent.parent:
        return None
    logging.warning(f'{bookmark.parent.title}.{bookmark.title}')
    children_titles: list[str] = __get_bookmarks_titles(bookmark.children)
    backup_children_titles: list[str] = __get_bookmarks_titles(backup_bookmark.children)

    found_titles: list[str] = []
    found_titles += __check_new_glas(children_titles, backup_children_titles=backup_children_titles)
    children_titles: list[str] = __remove_found_titles(children_titles, found_titles=found_titles)
    backup_children_titles: list[str] = __remove_found_titles(backup_children_titles, found_titles=found_titles)
    logging.error(f'- - -')
    found_titles += __check_new_slug(children_titles, backup_children_titles=backup_children_titles)
    children_titles: list[str] = __remove_found_titles(children_titles, found_titles=found_titles)
    backup_children_titles: list[str] = __remove_found_titles(backup_children_titles, found_titles=found_titles)
    logging.error(f'- - -')
    found_titles += __check_new(children_titles, backup_children_titles=backup_children_titles)
    children_titles: list[str] = __remove_found_titles(children_titles, found_titles=found_titles)
    backup_children_titles: list[str] = __remove_found_titles(backup_children_titles, found_titles=found_titles)


def __compare_bookmarks(
        bookmark_1: Bookmark,
        bookmark_2: Bookmark,
        __fun_compare_bookmarks
) -> None:
    __fun_compare_bookmarks(bookmark_1, bookmark_2)
    for sub_bookmark_1, sub_bookmark_2 in zip(bookmark_1.children, bookmark_2.children):
        __compare_bookmarks(sub_bookmark_1, sub_bookmark_2, __fun_compare_bookmarks)


def _compare_bookmarks(bookmarks_1: list[Bookmark], bookmarks_2: list[Bookmark], __fun_compare_bookmarks) -> None:
    for bookmark_1, bookmark_2 in zip(bookmarks_1, bookmarks_2):
        __compare_bookmarks(bookmark_1, bookmark_2, __fun_compare_bookmarks)


def _compare_pdf_with_backup_for_prolog(bookmarks: list[Bookmark], *, backup_bookmarks: list[Bookmark]) -> None:
    _compare_bookmarks(bookmarks, backup_bookmarks, __compare_bookmarks_for_prolog)


def _compare_pdf_with_backup_for_month_word(bookmarks: list[Bookmark], *, backup_bookmarks: list[Bookmark]) -> None:
    _compare_bookmarks(bookmarks, backup_bookmarks, __compare_bookmarks_for_month_word)


def _get_pdf_bookmarks_and_backup_bookmarks(
        pdf_path: Path,
        *,
        backup_pdf_path: Path
) -> tuple[list[Bookmark], list[Bookmark]]:
    bookmarks: list[Bookmark] = get_pdf_bookmarks(pdf_path)
    backup_bookmarks: list[Bookmark] = get_pdf_bookmarks(backup_pdf_path)
    return bookmarks, backup_bookmarks


def compare_pdf_with_backup_for_prolog(pdf_path: Path, *, backup_pdf_path: Path) -> None:
    bookmarks, backup_bookmarks = _get_pdf_bookmarks_and_backup_bookmarks(pdf_path, backup_pdf_path=backup_pdf_path)
    _compare_pdf_with_backup_for_prolog(bookmarks, backup_bookmarks=backup_bookmarks)


def compare_pdf_with_backup_for_month_word(pdf_path: Path, *, backup_pdf_path: Path) -> None:
    bookmarks, backup_bookmarks = _get_pdf_bookmarks_and_backup_bookmarks(pdf_path, backup_pdf_path=backup_pdf_path)
    bookmarks, backup_bookmarks = bookmarks[6].children, backup_bookmarks[6].children
    _compare_pdf_with_backup_for_month_word(bookmarks, backup_bookmarks=backup_bookmarks)


if __name__ == '__main__':
    # pdf_path = Path(r'C:\Users\MaxDroN\pravoslavie\lives_saints\prologs\prolog_sentyabr_fevral_3.pdf')
    # backup_pdf_path = Path(r'C:\Users\MaxDroN\pravoslavie\lives_saints\prologs\prolog_sentyabr_fevral_3_backup.pdf')
    # compare_pdf_with_backup_for_prolog(pdf_path, backup_pdf_path=backup_pdf_path)

    # pdf_path = Path(r"C:\Users\MaxDroN\Desktop\program\m\f-37-170___.pdf")
    # backup_pdf_path = Path(r"C:\Users\MaxDroN\python_projects\data\pdf\manuscripts\rsl\f_37\f-37-170_backup.pdf")
    pdf_path = Path(r"C:\Users\MaxDroN\python_projects\data\pdf\manuscripts\rsl\f_37\f-37-170.pdf")
    backup_pdf_path = Path(r"C:\Users\MaxDroN\python_projects\data\pdf\manuscripts\rsl\f_304i\f-304i-364.pdf")
    compare_pdf_with_backup_for_month_word(pdf_path, backup_pdf_path=backup_pdf_path)

