from pathlib import Path

from app.tests.const.year import main_1_split_on_bookmarks_and_prepare_title
from app.tests.create.prepare import main_4_join_bookmarks_and_sorted_by_pages_nums_and_delete_copy_elems, \
    LlsBookRusFullType, LlsBookRusType
from app.tests.crud import verify_all_lls_pages
from app.tests.schemas import main_2_add_brackets_and_offset_years
from app.tests.utils import main_3_offset_pages

__path = Path(r'C:\Users\MaxDroN\python_projects\app\delete_me\Output.md')
__encoding: str = 'utf-8'


def read_file(stem: str) -> str:
    path = __path.with_stem(stem)
    s = path.read_text(encoding=__encoding)
    return s


def write_file(out: str, *, stem: str) -> None:
    path = __path.with_stem(stem)
    path.write_text(out, encoding=__encoding)


def __main_1_split_on_bookmarks_and_prepare_title():
    s = read_file('Input_main_0')
    out = main_1_split_on_bookmarks_and_prepare_title(s)
    write_file(out, stem='Output_main_1')


def __main_2_add_brackets_and_offset_years():
    s = read_file('Output_main_1')
    out = main_2_add_brackets_and_offset_years(s)
    write_file(out, stem='Output_main_2')


def __main_3_offset_pages(num_offset_pages: int):
    s = read_file('Output_main_2')
    out = main_3_offset_pages(s, num_offset_pages=num_offset_pages)
    write_file(out, stem='Output_main_3')


def __main_4_join_bookmarks_and_sorted_by_pages_nums_and_delete_copy_elems(
        lls_book_rus: LlsBookRusFullType,
):
    s = read_file('Output_main_3')
    lls_book_rus_new: LlsBookRusType = [eval(i.strip()) for i in s.split(',\n')[:-1]]
    out = main_4_join_bookmarks_and_sorted_by_pages_nums_and_delete_copy_elems(
        lls_book_rus,
        lls_book_rus_new=lls_book_rus_new
    )
    write_file(out, stem='Output_main_4_FINAL')


if __name__ == '__main__':
    # __main_1_split_on_bookmarks_and_prepare_title()
    # __main_2_add_brackets_and_offset_years()
    __main_3_offset_pages(num_offset_pages=0)
    # __main_4_join_bookmarks_and_sorted_by_pages_nums_and_delete_copy_elems(const.lls_book_1)
    verify_all_lls_pages()
