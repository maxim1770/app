from sqlalchemy.orm import Session

from app import create
from app.db import base  # noqa: F401
from app.db.base_class import Base
from app.db.session import engine


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
    create.create_all_days(db)
    create.create_all_movable_dates(db)
    create.create_dates_for_years(db)
    create.create_all_holidays_categories(db)
    create.create_all_dignities(db)
    create.create_all_faces_sanctity(db)
    create.create_all_funds(db)
