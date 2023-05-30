def main_2_add_brackets_and_offset_years(s: str) -> str:
    out = ''
    for i in s.split('\n'):
        i = i.strip()
        if i == '':
            continue
        if '!!!' in i:
            title, year = i.split('!!!')
            title = title.strip()
            year = year.strip()
            year = int(year) - 8
            out += f"    (('{title}', {year}), )," + '\n'
            continue
        out += f"    ('{i}', )," + '\n'
    return out


def main_3_offset_pages(s, *, num_offset_pages: int = 4) -> str:
    out = ''
    for i in s.split('\n'):
        if not i or i == ' ':
            continue
        if i.strip() == '-':
            # print(i)
            continue
        page_str = i[-5:-2].strip()
        if ',' in page_str:
            page_str = page_str.replace(',', '').strip()
        page = int(page_str)
        page_new = page - num_offset_pages
        out += i.replace(str(page), str(page_new)) + '\n'
    return out


import logging

from app.tests import const
from app.tests.const import LlsBookRusFullType


def verify_pages_in_lls_book_rus(lls_book_rus: LlsBookRusFullType) -> bool:
    l = lls_book_rus[0]
    l_sorted = sorted(l, key=lambda tuple_: tuple_[-1])
    if l_sorted != l:
        logging.error('ЛИСТЫ НЕ ПО ПОРЯДКУ')
        raise ValueError('ЛИСТЫ НЕ ПО ПОРЯДКУ')
    return True


def verify_all_lls_pages():
    for lls_book_rus in [
        const.lls_book_rus_1,
        const.lls_book_rus_2,
        const.lls_book_rus_3,
        const.lls_book_rus_4,
        const.lls_book_rus_5,
        const.lls_book_rus_6,
        const.lls_book_rus_7,
        const.lls_book_rus_8,
        const.lls_book_rus_9,
        const.lls_book_rus_10,
        const.lls_book_rus_11,
        const.lls_book_rus_12,
        const.lls_book_rus_13,
        const.lls_book_rus_14,
        const.lls_book_rus_15,
        const.lls_book_rus_16,
        const.lls_book_rus_17,
        const.lls_book_rus_18,
        const.lls_book_rus_19,
        const.lls_book_rus_20,
        const.lls_book_rus_21,
        const.lls_book_rus_22,
        const.lls_book_rus_23,
    ]:
        verify_pages_in_lls_book_rus(lls_book_rus)


from pathlib import Path

from app.tests.const.year import main_1_split_on_bookmarks_and_prepare_title
from app.tests.create.prepare import main_4_join_bookmarks_and_sorted_by_pages_nums_and_delete_copy_elems, \
    LlsBookRusFullType, LlsBookRusType
from app.tests.crud import verify_all_lls_pages
from app.tests.schemas import main_2_add_brackets_and_offset_years, main_3_offset_pages

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

from app.tests import const
from app.tests.const import LlsBookRusType, LlsBookRusFullType


def _main_4_join_bookmarks_and_sorted_by_pages_nums_and_delete_copy_elems(lls_book_rus: LlsBookRusFullType, *,
                                                                          lls_book_rus_new: LlsBookRusType) -> LlsBookRusType:
    """"
    ВАЖНО
        ('О приходе великой княгини с Белоозера', 498),
        ('О кончине Ростовского архиепископа', 498),
    Две разные закладки на одной странице, поэтому нельзя оставлять только одну закладку на одной странице в массиве commom_list

    НО МОЖНО ТАМ ПРОВЕРЯТЬ НА СООТВЕТСВИЯ СТРОКИ И ГОДА, И ТОГДА ВСЕ ОК, ЕСЛИ ВСЕ СОВПАЛО, ТО МОЖНО УБИРАТЬ, ОДНУ ИЗ ЗАКЛАДКО (КОТОРАЯ ИЗ lls_book_rus СКОРЕЕ СТОИТ УБИРАТЬ)
    """
    lls_book_rus = lls_book_rus[0]
    commom_list: LlsBookRusType = lls_book_rus + lls_book_rus_new
    commom_list = sorted(commom_list, key=lambda tuple_: tuple_[-1])
    commom_list = list(dict.fromkeys(commom_list))
    return commom_list


def main_4_join_bookmarks_and_sorted_by_pages_nums_and_delete_copy_elems(lls_book_rus: LlsBookRusFullType, *,
                                                                         lls_book_rus_new: LlsBookRusType) -> str:
    join_lls_book_rus = _main_4_join_bookmarks_and_sorted_by_pages_nums_and_delete_copy_elems(lls_book_rus,
                                                                                              lls_book_rus_new=lls_book_rus_new)
    out = ''
    for index, i in enumerate(join_lls_book_rus):
        if index + 1 < len(join_lls_book_rus) and join_lls_book_rus[index + 1][-1] == i[-1]:
            out += '\n'
        out += '        '
        out += str(i)
        if i == join_lls_book_rus[-1]:
            continue
        out += ',' + '\n'
        if join_lls_book_rus[index - 1][-1] == i[-1]:
            out += '\n'
    return out


lls_book_rus_new: LlsBookRusType = (
    [
        ('О преставлении князя Юрия Васильевича', 404),
        ('Приход царевны Софьи на Москву', 409),
        ('Свадьба великого князя Ивана Васильевича', 417),
        ('О венецианском после Тревизане', 426),
        ('О кончине Филиппа митрополита и о пожаре', 432),
        ('О поставлении Геронтия на митрополию', 445),
        ('О ростовских князьях', 478)
    ], 4)

if __name__ == '__main__':
    main_4_join_bookmarks_and_sorted_by_pages_nums_and_delete_copy_elems(const.lls_book_rus_16,
                                                                         lls_book_rus_new=lls_book_rus_new)

if __name__ == '__main__':
    s = """

    """
    print(main_2_add_brackets_and_offset_years(s))

    s = """
    """
    main_3_offset_pages(s)
