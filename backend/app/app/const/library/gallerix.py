from enum import StrEnum


class GallerixUrl(StrEnum):
    SOME_ICON_ID = 'some_icon_id'
    _DOMAIN = 'https://gallerix.ru'
    _DOMAIN_FOR_GET_ICON_IMG = 'https://sr.gallerix.ru'
    GET_SAINTS = f'{_DOMAIN}/album/ikony'
    GET_ICON_DATA = f'{GET_SAINTS}/pic/glrx-{SOME_ICON_ID}'
    GET_ICON_IMG = f'{_DOMAIN_FOR_GET_ICON_IMG}/_UNK/4221350301/{SOME_ICON_ID}.jpg'

# https://gallerix.ru/fullpic/c9abd8e796ade3a2fdf39a3e6d8a36c6/ хорошее качество Икон
# https://gallerix.ru/fullpic/f26074f014ad425af1168f4857adcde0/
# https://gallerix.ru/fullpic/56bd33710a1727879092ab25f6f16c25/