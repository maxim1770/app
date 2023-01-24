from sqlalchemy.orm import Session

from app.create.create.day import create_all_days
from app.create.create.holiday.holiday_category import create_all_holidays_categories
from app.db import base  # noqa: F401
from app.db.base_class import Base
from app.db.session import engine


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
    create_all_days(db)
    create_all_holidays_categories(db)
