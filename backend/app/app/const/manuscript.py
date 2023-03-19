import re
from enum import StrEnum
from typing import Pattern


class NlrUrl(StrEnum):
    DOMAIN = 'https://nlr.ru'
    _MANUSCRIPT_BASE = f'{DOMAIN}/manuscripts'
    GET_MANUSCRIPT = f'{_MANUSCRIPT_BASE}/RA1527/elektronnyiy-katalog'
    __MANUSCRIPT_API_BASE = f'{_MANUSCRIPT_BASE}/1/1/ajax'
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


REGEX_RSL_MANUSCRIPT_CODE_STR: str = r'^f-\d{1,3}i{0,3}-\d{1,4}$'
REGEX_RSL_MANUSCRIPT_CODE: Pattern[str] = re.compile(REGEX_RSL_MANUSCRIPT_CODE_STR)
