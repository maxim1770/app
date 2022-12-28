from app import models, schemas
from sqlalchemy.orm import Session


def get_holidays_categories(db: Session, skip: int = 0, limit: int = 100) -> list[models.HolidayCategory]:
    return db.query(models.HolidayCategory).offset(skip).limit(limit).all()


def get_holiday_category(db: Session, title: schemas.HolidayCategoryTitle) -> models.HolidayCategory | None:
    return db.query(models.HolidayCategory).filter(models.HolidayCategory.title == title).first()


def create_holiday_category(db: Session, holiday_category: schemas.HolidayCategoryCreate) -> models.HolidayCategory:
    db_holiday_category: models.HolidayCategory = models.HolidayCategory(**holiday_category.dict())
    db.add(db_holiday_category)
    db.commit()
    db.refresh(db_holiday_category)
    return db_holiday_category
