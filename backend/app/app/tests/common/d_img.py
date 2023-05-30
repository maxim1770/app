import logging

import requests
from sqlalchemy.orm import Session

from app.api import deps

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

from app.create.create.icon.create_icon_imgs import create_all_icons_imgs

if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    db: Session = next(deps.get_db())
    create_all_icons_imgs(db, session=session)
