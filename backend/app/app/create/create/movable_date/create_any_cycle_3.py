import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import crud, schemas, enums
from app import models


def create_any_cycle_3(db):
    _create_c3_liturgies_on_sat_and_sun(db)
    _create_c3_matins_on_sun_6(db)
    _create_all_strastnaja_sedmitsa(db)


def _create_c3_liturgies_on_sat_and_sun(db: Session):
    movable_days = db.execute(sa.select(models.MovableDay).join(models.Week).join(models.Cycle).filter(
        (models.Cycle.num == enums.CycleNum.cycle_3) &
        (models.Week.title.not_like('%Страстная%')) &
        (
                (models.MovableDay.abbr == enums.MovableDayAbbr.sat) |
                (models.MovableDay.abbr == enums.MovableDayAbbr.sun)
        )
    ).order_by(models.MovableDay.id)).scalars().all()
    for movable_day in movable_days:
        crud.create_movable_date(
            db,
            movable_day_id=movable_day.id,
            divine_service_title=enums.DivineServiceTitle.liturgy
        )


def _create_c3_matins_on_sun_6(db: Session):
    sun_6 = db.execute(sa.select(models.MovableDay).join(models.Week).join(models.Cycle).filter(
        (models.Cycle.num == enums.CycleNum.cycle_3) &
        (models.Week.sunday_num == 6) &
        (models.MovableDay.abbr == enums.MovableDayAbbr.sun)
    )).scalar_one_or_none()
    crud.create_movable_date(
        db,
        movable_day_id=sun_6.id,
        divine_service_title=enums.DivineServiceTitle.matins
    )


def _create_all_strastnaja_sedmitsa(db: Session):
    week_in = schemas.WeekCreate(
        title='Страстная седмица',
    )
    cycle = crud.get_cycle(db, num=enums.CycleNum.cycle_3)
    week = crud.create_week(db, cycle_id=cycle.id, week=week_in)
    week_id: int = week.id

    movable_days: list[models.MovableDay] = []
    movable_days.append(
        crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(
            abbr=enums.MovableDayAbbr.mon,
            title=enums.MovableDayStrastnajaSedmitsaRu.mon.value
        )))
    movable_days.append(
        crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(
            abbr=enums.MovableDayAbbr.tue,
            title=enums.MovableDayStrastnajaSedmitsaRu.tue.value
        )))
    movable_days.append(
        crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(
            abbr=enums.MovableDayAbbr.wed,
            title=enums.MovableDayStrastnajaSedmitsaRu.wed.value
        )))
    thu = crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(
        abbr=enums.MovableDayAbbr.thu,
        title=enums.MovableDayStrastnajaSedmitsaRu.thu.value
    ))
    movable_days.append(thu)
    crud.create_movable_date(
        db,
        movable_day_id=thu.id,
        divine_service_title=enums.DivineServiceTitle.vespers
    )
    crud.create_movable_date(
        db,
        movable_day_id=thu.id
    )
    # Создаем fri тут, чтобы в бд строчки были по порядку чт-пт-сб
    fri = crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(
        abbr=enums.MovableDayAbbr.fri,
        title=enums.MovableDayStrastnajaSedmitsaRu.fri.value
    ))
    sat = crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(
        abbr=enums.MovableDayAbbr.sat,
        title=enums.MovableDayStrastnajaSedmitsaRu.sat.value
    ))
    movable_days.append(sat)
    crud.create_movable_date(
        db,
        movable_day_id=sat.id,
        divine_service_title=enums.DivineServiceTitle.matins
    )
    for movable_day in movable_days:
        crud.create_movable_date(
            db,
            movable_day_id=movable_day.id,
            divine_service_title=enums.DivineServiceTitle.liturgy
        )
    __create_fri_strastnaja_sedmitsa_movable_dates(db, fri=fri)


def __create_fri_strastnaja_sedmitsa_movable_dates(db: Session, *, fri: models.MovableDay):
    crud.create_movable_date(
        db,
        movable_day_id=fri.id
    )
    crud.create_movable_date(
        db,
        movable_day_id=fri.id,
        divine_service_title=enums.DivineServiceTitle.vespers
    )
    ...
