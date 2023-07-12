import re
from enum import StrEnum, IntEnum
from typing import Pattern


class NlrUrl(StrEnum):
    DOMAIN = 'https://nlr.ru'
    MANUSCRIPT_BASE = f'{DOMAIN}/manuscripts'
    GET_MANUSCRIPT = f'{MANUSCRIPT_BASE}/RA1527/elektronnyiy-katalog'
    __MANUSCRIPT_API_BASE = f'{MANUSCRIPT_BASE}/1/1/ajax'
    GET_MANUSCRIPT_DATA_API = f'{__MANUSCRIPT_API_BASE}/GetResultDocumPoiskCatalogueOne'
    GET_MANUSCRIPT_PAGES_API = f'{__MANUSCRIPT_API_BASE}/GetResultDocumPoiskCatalogueOneIzo'
    SEARCH_MANUSCRIPT_API = f'{__MANUSCRIPT_API_BASE}/GetResultDocumPoiskCatalogue'


class RslUrl(StrEnum):
    _DOMAIN = 'https://lib-fond.ru'
    GET_MANUSCRIPT = f'{_DOMAIN}/lib-rgb'
    SEARCH_MANUSCRIPT = f'{_DOMAIN}/search'


class NebUrl(StrEnum):
    DOMAIN = 'https://kp.rusneb.ru'
    __GET_MANUSCRIPT_BASE = f'{DOMAIN}/item'
    GET_MANUSCRIPT_DATA = f'{__GET_MANUSCRIPT_BASE}/material'
    GET_MANUSCRIPT_PAGES = f'{__GET_MANUSCRIPT_BASE}/reader'
    SEARCH_MANUSCRIPT_API = f'{DOMAIN}/search/2/facets'


class RuniversUrl(StrEnum):
    _DOMAIN = 'https://runivers.ru'
    _LIB = f'{_DOMAIN}/lib'
    GET_MANUSCRIPT_PAGES = f'{_DOMAIN}/bookreader/books'
    GET_ALl_Lls = f'{_LIB}/book6958'
    GET_ALl_Lls_FOR_RUS_1_10 = f'{_LIB}/book19785'


class RuniversLlsId(IntEnum):
    lls_book_1 = 197389
    lls_book_2 = 197391
    lls_book_3 = 197394
    lls_book_4 = 197396  # TODO добавил для manuscript.url (вообще там перемешанные листы на сайте)
    lls_book_5 = 197398
    lls_book_6 = 477701
    lls_book_7 = 477711
    lls_book_8 = 477717
    lls_book_9 = 478157
    lls_book_10 = 478159

    # lls_book_rus_1 = 478161  # Русь Книга 1 (Тут получается Русь Книга 1-2)

    # - - -
    # С lls_book_rus_1 (594254) по lls_book_rus_10 Собираем из другого издания id = 19785
    # https://runivers.ru/lib/book19785

    lls_book_rus_1 = 594254  # Совпадают
    lls_book_rus_2 = 594256  # Совпадают
    lls_book_rus_3 = 594196  # 1182 (1174) - 1212 (1204), а у Германа 1183 (1175) - 1213 (1205)
    lls_book_rus_4 = 594201  # Совпадают
    lls_book_rus_5 = 594203  # Заканчивается на 1249 (1241), а у Германа на 1248 (1240)
    lls_book_rus_6 = 594258  # Начинается с 1250 (1242), а у Германа с 1248 (1240)
    lls_book_rus_7 = 594260  # Совпадают
    lls_book_rus_8 = 594265  # Совпадают
    lls_book_rus_9 = 594267  # Совпадают
    lls_book_rus_10 = 594269  # Совпадают

    # - - -

    lls_book_rus_11 = 480116  # Русь Книга 11
    lls_book_rus_12 = 480190
    lls_book_rus_13 = 480292
    lls_book_rus_14 = 480448
    lls_book_rus_15 = 480451
    lls_book_rus_16 = 480453
    lls_book_rus_17 = 481263
    lls_book_rus_18 = 481313
    lls_book_rus_19 = 481461
    lls_book_rus_20 = 481478
    lls_book_rus_21 = 481997
    lls_book_rus_22 = 482205
    lls_book_rus_23 = 482514  # Русь Книга 23


REGEX_RSL_MANUSCRIPT_CODE_STR: str = r'^f-\d{1,3}i{0,3}-\d{1,4}$'
REGEX_RSL_MANUSCRIPT_CODE: Pattern[str] = re.compile(REGEX_RSL_MANUSCRIPT_CODE_STR)

__regex_rsl = r"""(?x)             # Позволяет писать комментарии внутри рег. выр. Подробнее тут: https://stackoverflow.com/a/20669086/19440443
(?<=^)
(?:\d+(?:-i+)?)           # Проверка первой части - шифра: цифры, потом (тире с i одной или много) ИЛИ (ничего)
/                         # Разделение пути в url
(?:f-(?:\d+(?:i+)?)-\d+)  # Формат записи ед. хранения f-, потом так же как шифр, только без тире, после -\d
/?                        # ТАК ЖЕ ВОЗМОЖЕН "/" В КОНЦЕ СТРОКИ, ДЛЯ УДОБСТВА, В pathlib он убирается и все ок, НО С str НУЖНО БЫТО ОСТОРОЖНЫМ
(?=$)
"""
