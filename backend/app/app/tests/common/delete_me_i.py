import logging

import requests
from sqlalchemy.orm import Session

from app.api import deps
from app.create.create.icon.create_all import create_all_icons

logging.basicConfig(level=logging.ERROR, format='%(levelname)s:%(message)s')


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    session: requests.Session = next(deps.get_session())
    create_all_icons(db, session=session)
