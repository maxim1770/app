import logging

import requests
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from .saint import update_saint_from_azbyka
from ..base_cls import FatalCreateError


def update_saints(db: Session) -> None:
    saints = crud.saint.get_multi(db, limit=100_000)
    session: requests.Session = next(deps.get_session())
    for saint in saints:
        try:
            saint = update_saint_from_azbyka(db, session=session, saint=saint)
        except FatalCreateError as e:
            logging.warning(e.args[0])
