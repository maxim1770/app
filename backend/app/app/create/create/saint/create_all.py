import logging

import requests
from sqlalchemy.orm import Session

from app import crud
from .saint import update_saint_from_azbyka
from ..base_cls import FatalCreateError


def update_saints(db: Session, *, session: requests.Session) -> None:
    saints = crud.saint.get_multi(db, limit=10_000)
    for saint in saints:
        try:
            saint = update_saint_from_azbyka(db, session=session, saint=saint)
        except FatalCreateError as e:
            logging.warning(e.args[0])
