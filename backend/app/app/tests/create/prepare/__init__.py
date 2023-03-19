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
