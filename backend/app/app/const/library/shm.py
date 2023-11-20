from enum import StrEnum


class ShmUrl(StrEnum):
    SOME_ITEM_ID = 'some_item_id'
    SOME_PAGE = 'some_page'
    SOME_FUND_IER = 'some_fund_ier'
    _DOMAIN = 'https://catalog.shm.ru'
    GET_ITEMS = f'{_DOMAIN}/entity/OBJECT?page={SOME_PAGE}&fund_ier={SOME_FUND_IER}'
    GET_ITEM_DATA = f'{_DOMAIN}/entity/OBJECT/{SOME_ITEM_ID}'
    GET_ITEM_IMG = f'{GET_ITEM_DATA}/entity/OBJECT/{SOME_ITEM_ID}'


