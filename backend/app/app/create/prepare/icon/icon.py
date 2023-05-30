import requests
from pydantic import ValidationError

from app import schemas, enums, models
from .get_icon_data_in import get_pravicon_icons_ids, get_pravicon_icon_data_in
from ._get_pravicon_saints_ids import get_pravicon_saints_ids


def get_saints_icons_data_in(session: requests.Session, *, saints: list[models.Saint]) -> list[schemas.IconDataCreate]:
    saints_icons_data_in: list[schemas.IconDataCreate] = []
    for saint, pravicon_saint_id in get_pravicon_saints_ids(session, saints=saints):
        saint_icons_data_in: list[schemas.IconDataCreate] = []
        holiday_slug = [holiday.slug for holiday in saint.holidays if
                        holiday.holiday_category.title == enums.HolidayCategoryTitle.den_pamjati][0]
        pravicon_icons_ids: list[int] = get_pravicon_icons_ids(session, pravicon_saint_id=pravicon_saint_id)
        for pravicon_icon_id in pravicon_icons_ids:
            try:
                icon_data_in: schemas.IconDataCreate = get_pravicon_icon_data_in(
                    session,
                    pravicon_icon_id=pravicon_icon_id,
                    holiday_slug=holiday_slug
                )
            except (AttributeError, ValidationError):
                continue
            else:
                saint_icons_data_in.append(icon_data_in)
        saints_icons_data_in += saint_icons_data_in
    return saints_icons_data_in
