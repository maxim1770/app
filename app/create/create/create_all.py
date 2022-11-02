from sqlalchemy.orm import Session

from app.api import deps
from app.create.create.movable_date.create_all import create_all_movable_dates


def create_all(db: Session):
    create_all_movable_dates(db)


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    create_all(db)
