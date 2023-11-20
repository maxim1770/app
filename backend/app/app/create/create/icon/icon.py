from sqlalchemy.orm import Session

from app import schemas, models, crud


def create_icon(
        db: Session, *, icon_data_in: schemas.IconDataCreate
) -> models.Icon:
    holiday = crud.holiday.get_by_slug(db, slug=icon_data_in.holiday_slug)
    year = crud.year.get_or_create(db, year_in=icon_data_in.year_in)
    city_id: int | None = crud.city.get_by_title(
        db,
        title=icon_data_in.city_title
    ).id if icon_data_in.city_title else None
    icon = crud.icon.create_with_any(
        db,
        obj_in=icon_data_in.icon_in,
        year_id=year.id,
        city_id=city_id
    )
    icon = crud.icon.create_holiday_association(
        db,
        db_obj=icon,
        holiday=holiday,
        icon_holiday_association_in=schemas.IconHolidayAssociationCreate()
    )
    return icon
