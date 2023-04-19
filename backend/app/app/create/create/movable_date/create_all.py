import logging

from sqlalchemy.orm import Session

from app import crud, schemas, enums
from app.create import prepare
from .cycle import create_cycles
from .divine_service import create_divine_services
from .movable_date import CreateMovableDate
from .movable_day import CreateMovableDay
from .week import CreateWeek


def create_all_movable_dates(db: Session):
    create_cycles(db)
    logging.info("Created cycles")

    create_divine_services(db)
    logging.info("Created divine services")

    create_all_c1_movable_dates(db)

    create_all_c2_movable_dates(db)

    create_all_c3_movable_dates(db)


def create_all_c1_movable_dates(db: Session):
    cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_1).id

    create_week: CreateWeek = prepare.CreateWeekFactory.get_c1_week(db, cycle_id=cycle_id)
    weeks_id: list[int] = create_week.create()
    logging.info("Created c1 weeks")

    create_day: CreateMovableDay = prepare.CreateMovableDayFactory.get_c1_day(db, weeks_id=weeks_id)
    days_id: list[int] = create_day.create()
    logging.info("Created c1 days")

    crud.create_movable_date(
        db,
        movable_day_id=crud.get_movable_day_(
            db,
            movable_day_get=schemas.MovableDayGet(
                cycle_num=enums.CycleNum.cycle_1,
                sunday_num=1,
                abbr=enums.MovableDayAbbr.sun
            )
        ).id,
        divine_service_title=enums.DivineServiceTitle.vespers,
        movable_date=schemas.MovableDateCreate()
    )
    create_movable_date: CreateMovableDate = prepare.CreateMovableDateFactory.get_c1_movable_date(db, days_id=days_id)
    movable_dates_id: list[int] = create_movable_date.create()
    logging.info("Created c1 movable dates")


def create_all_c2_movable_dates(db: Session):
    cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_2).id

    create_week: CreateWeek = prepare.CreateWeekFactory.get_c2_week(db, cycle_id=cycle_id)
    weeks_id: list[int] = create_week.create()
    logging.info("Created c2 weeks")

    create_day: CreateMovableDay = prepare.CreateMovableDayFactory.get_c2_day(db, weeks_id=weeks_id)
    days_id: list[int] = create_day.create()
    logging.info("Created c2 days")

    create_movable_date: CreateMovableDate = prepare.CreateMovableDateFactory.get_c2_movable_date(db, days_id=days_id)
    movable_dates_id: list[int] = create_movable_date.create()
    logging.info("Created c2 movable dates")


def create_all_c3_movable_dates(db: Session):
    cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_3).id

    create_week: CreateWeek = prepare.CreateWeekFactory.get_c3_week(db, cycle_id=cycle_id)
    weeks_id: list[int] = create_week.create()
    logging.info("Created c3 weeks")

    create_day: CreateMovableDay = prepare.CreateMovableDayFactory.get_c3_day(db, weeks_id=weeks_id)
    days_id: list[int] = create_day.create()
    logging.info("Created c3 days")

    create_strastnaja_sedmitsa(db)
    logging.info("Created  strastnaja_sedmitsa week")
    logging.info("Created strastnaja_sedmitsa days")

    # create_movable_date: CreateMovableDate = prepare.CreateMovableDateFactory.get_c3_movable_date(db, days_id=days_id)
    # movable_dates_id: list[int] = create_movable_date.create()
    # logging.info("Created c3 movable dates")


def create_strastnaja_sedmitsa(db: Session):
    week_in = schemas.WeekCreate(
        title='Страстная седмица',
    )
    week = crud.create_week(db, cycle_id=enums.CycleNum.cycle_3, week=week_in)
    week_id: int = week.id

    crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(abbr=enums.MovableDayAbbr.mon))
    crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(abbr=enums.MovableDayAbbr.tue))
    crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(abbr=enums.MovableDayAbbr.wed))
    crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(abbr=enums.MovableDayAbbr.thu))
    crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(
        abbr=enums.MovableDayAbbr.fri,
        title='Святая и Великая Пятница'
    )
                            )
    crud.create_movable_day(db, week_id=week_id, movable_day=schemas.MovableDayCreate(abbr=enums.MovableDayAbbr.sat))
