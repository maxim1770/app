import logging

from sqlalchemy.orm import Session

from app import crud, enums, schemas
from app.create import prepare
from .create_any_cycle_3 import create_any_cycle_3
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
    _create_all_c1_movable_dates(db)
    _create_all_c2_movable_dates(db)
    _create_all_c3_movable_dates(db)


def _create_all_c1_movable_dates(db: Session) -> None:
    cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_1).id

    create_week: CreateWeek = prepare.CreateWeekFactory.get_c1_week(db, cycle_id=cycle_id)
    weeks_id: list[int] = create_week.create()
    logging.info("Created c1 weeks")

    create_day: CreateMovableDay = prepare.CreateMovableDayFactory.get_c1_day(db, weeks_id=weeks_id)
    days_id: list[int] = create_day.create()
    logging.info("Created c1 days")

    create_movable_date: CreateMovableDate = prepare.CreateMovableDateFactory.get_c1_movable_date(db, days_id=days_id)
    movable_dates_id: list[int] = create_movable_date.create()
    crud.create_movable_date(
        db,
        movable_day_id=crud.get_movable_day(
            db,
            movable_day_get=schemas.MovableDayGet(
                cycle_num=enums.CycleNum.cycle_1,
                sunday_num=1,
                abbr=enums.MovableDayAbbr.sun
            )
        ).id,
        divine_service_title=enums.DivineServiceTitle.vespers
    )
    logging.info("Created c1 movable dates")


def _create_all_c2_movable_dates(db: Session) -> None:
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


def _create_all_c3_movable_dates(db: Session) -> None:
    cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_3).id

    create_week: CreateWeek = prepare.CreateWeekFactory.get_c3_week(db, cycle_id=cycle_id)
    weeks_id: list[int] = create_week.create()
    logging.info("Created c3 weeks")

    create_day: CreateMovableDay = prepare.CreateMovableDayFactory.get_c3_day(db, weeks_id=weeks_id)
    days_id: list[int] = create_day.create()
    logging.info("Created c3 days")

    create_any_cycle_3(db)
    logging.info('Created c3 any movable_dates and strastnaja sedmitsa')
