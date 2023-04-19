from enum import StrEnum


class AzbykaUrl(StrEnum):
    DOMAIN = 'https://azbyka.ru'
    DAYS = f'{DOMAIN}/days'
    GET_ZACHALO = f'{DOMAIN}/biblia/?'
    GET_SAINT_BY_SLUG = f'{DAYS}/sv-'
    GET_SAINT_BY_ID = f'{DAYS}/saint'
    GET_HOLIDAYS_IN_DAY_API = f'{DAYS}/widgets/presentations.json?date='
