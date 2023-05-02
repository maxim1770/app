from app.create import const


def _prepare_pravicon_saint_icons_url(pravicon_saint_id: int) -> str:
    pravicon_saint_icons_url: str = const.PraviconUrl.GET_SAINT_ICONS.replace(
        const.PraviconUrl.SOME_SAINT_ID, str(pravicon_saint_id)
    )
    return pravicon_saint_icons_url


def _prepare_pravicon_icon_data_url(pravicon_icon_id: int) -> str:
    pravicon_icon_data_url: str = const.PraviconUrl.GET_ICON_DATA.replace(
        const.PraviconUrl.SOME_ICON_ID, str(pravicon_icon_id)
    )
    return pravicon_icon_data_url


def _prepare_pravicon_icon_img_url(pravicon_icon_id: int) -> str:
    pravicon_icon_img_url: str = const.PraviconUrl.GET_ICON_IMG.replace(
        const.PraviconUrl.SOME_ICON_DIR_NUM, str(pravicon_icon_id // 1000)
    ).replace(
        const.PraviconUrl.SOME_ICON_ID, str(pravicon_icon_id)
    )
    return pravicon_icon_img_url
