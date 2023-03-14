from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import FatalCreateError


def create_all_holidays_categories(db: Session) -> None:
    if crud.get_holidays_categories(db):
        raise FatalCreateError(f'HolidayCategory: holidays_categories уже были созданы')

    holidays_categories_in = [schemas.HolidayCategoryCreate(title=holiday_category_title)
                              for holiday_category_title in enums.HolidayCategoryTitle]

    for holiday_category_in in holidays_categories_in:
        crud.create_holiday_category(db, holiday_category_in=holiday_category_in)
