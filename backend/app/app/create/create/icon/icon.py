from sqlalchemy.orm import Session

from app import schemas, models, crud


def create_icon(
        db: Session, *, icon_data_in: schemas.IconDataCreate
) -> models.Icon:
    holiday = crud.holiday.get_by_slug(db, slug=icon_data_in.holiday_slug)
    year = crud.get_or_create_year(db, year_in=icon_data_in.year_in)
    city_id: int | None = crud.get_city(db, title=icon_data_in.city_title).id if icon_data_in.city_title else None
    icon = crud.icon.create_with_any(
        db,
        obj_in=icon_data_in.icon_in,
        holiday_id=holiday.id,
        year_id=year.id,
        city_id=city_id
    )
    return icon
