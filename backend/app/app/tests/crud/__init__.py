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
