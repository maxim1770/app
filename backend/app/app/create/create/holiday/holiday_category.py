from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import FatalCreateError


def create_all_holidays_categories(db: Session) -> None:
    if crud.holiday_category.get_all(db):
        raise FatalCreateError(f'HolidayCategory: holidays_categories already created')
    holidays_categories_in = [
        schemas.HolidayCategoryCreate(title=holiday_category_title)
        for holiday_category_title in enums.HolidayCategoryTitle
    ]
    for holiday_category_in in holidays_categories_in:
        crud.holiday_category.create(db, obj_in=holiday_category_in)
