from enum import StrEnum


class PraviconUrl(StrEnum):
    SOME_SAINT_ID = 'some_saint_id'
    SOME_ICON_ID = 'some_icon_id'
    SOME_ICON_DIR_NUM = 'some_icon_dir_num'
    _DOMAIN = 'http://pravicon.com'
    GET_SAINTS = f'{_DOMAIN}/s'
    GET_SAINT_DESC = f'{_DOMAIN}/icon-'
    GET_SAINT_ICONS = f'{GET_SAINT_DESC}{SOME_SAINT_ID}-photo'
    GET_ICON_DATA = f'{_DOMAIN}/image-{SOME_ICON_ID}'
    GET_ICON_IMG = f'{_DOMAIN}/images/icons/{SOME_ICON_DIR_NUM}/{SOME_ICON_ID}.jpg'
