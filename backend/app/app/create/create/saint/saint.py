from typing import Any

import requests
from sqlalchemy.orm import Session

from app import crud, models, schemas
from ..base_cls import FatalCreateError
from ...prepare import SaintDataUpdateFactory


def create_saint(db: Session, *, saint_data_in: schemas.SaintDataCreate) -> models.Saint:
    foreign_keys: dict[str, int] = {}
    if saint_data_in.face_sanctity_title:
        face_sanctity = crud.get_face_sanctity(db, title=saint_data_in.face_sanctity_title)
        foreign_keys |= {'face_sanctity_id': face_sanctity.id}
    if saint_data_in.dignity_title:
        dignity = crud.get_dignity(db, title=saint_data_in.dignity_title)
        foreign_keys |= {'dignity_id': dignity.id}
    saint = crud.saint.create_with_any(
        db,
        obj_in=saint_data_in.saint_in,
        **foreign_keys
    )
    return saint


def update_saint(
        db: Session,
        *,
        saint: models.Saint,
        saint_data_in: schemas.SaintDataUpdate
) -> models.Saint:
    obj_in: dict[str, Any] = {}
    if saint_data_in.saint_in:
        obj_in |= saint_data_in.saint_in.dict(exclude_none=True)
    if saint_data_in.face_sanctity_title:
        face_sanctity = crud.get_face_sanctity(db, title=saint_data_in.face_sanctity_title)
        obj_in |= {'face_sanctity_id': face_sanctity.id}
    if saint_data_in.dignity_title:
        dignity = crud.get_dignity(db, title=saint_data_in.dignity_title)
        obj_in |= {'dignity_id': dignity.id}
    saint = crud.saint.update(db, db_obj=saint, obj_in=obj_in)
    return saint


def update_saint_from_azbyka(db: Session, *, session: requests.Session, saint: models.Saint) -> models.Saint:
    if saint.name:
        raise FatalCreateError(f'Saint name already exists, saint.slug = {saint.slug}')
    if saint.slug == 'kallisfenija-efesskaja':
        saint_data_in = schemas.SaintDataUpdate(saint_in=schemas.SaintUpdate(name='Каллисфе́ния Ефесская'))
    elif saint.slug == 'markellin-ispanskij':
        saint_data_in = schemas.SaintDataUpdate(saint_in=schemas.SaintUpdate(name='Маркелли́н Испанский'))
    else:
        saint_data_in = SaintDataUpdateFactory(session=session, saint_slug=saint.slug).get()
    saint = update_saint(db, saint=saint, saint_data_in=saint_data_in)
    return saint
