import logging

import requests
from sqlalchemy.orm import Session

from app import crud, enums
from app.api import deps

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    db: Session = next(deps.get_db())
    for icon in crud.icon.get_multi(db, limit=3000):
        if enums.HolidayCategoryTitle.perenesenie_moschej in icon.desc:
            logging.info(icon.desc)
