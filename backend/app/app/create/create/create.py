import requests
from sqlalchemy.orm import Session

from app import create
from app.api import deps


def create_all_holidays(db: Session, session: requests.Session):
    create.create_all_saints_holidays(db)
    create.create_all_great_holidays(db)
    create.create_all_movable_saints_holidays(db)
    create.create_all_cathedrals_saints(db)
    create.create_any_holidays(db)
    create.create_all_proroks_and_any_pravednyjs(db)
    # create.create_all_saints_groups_holidays(db, session)


def main(db: Session, session: requests.Session):
    create_all_holidays(db, session)
    # create.update_saints(db)


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    session: requests.Session = next(deps.get_session())
    main(db, session)
