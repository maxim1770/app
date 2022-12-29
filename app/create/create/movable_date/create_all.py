import logging

from sqlalchemy.orm import Session

from app import schemas, crud, enums
from app.api import deps
from app.create import prepare
from app.create.create.movable_date.cycle import create_cycles
from app.create.create.movable_date.movable_day import CreateMovableDay
from app.create.create.movable_date.divine_service import create_divine_services
from app.create.create.movable_date.movable_date import CreateMovableDate
from app.create.create.movable_date.week import CreateWeek
from app.db.session import engine, Base


# TODO подумать над тем чтобы начинать использовать tuple там где это можно делать

def create_all_movable_dates(db: Session):
    create_cycles(db)
    logging.info("Create cycles")

    create_divine_services(db)
    logging.info("Create divine services")

    create_all_c1_movable_dates(db)

    create_all_c2_movable_dates(db)

    create_all_c3_movable_dates(db)


def create_all_c1_movable_dates(db: Session):
    cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_1).id

    create_week: CreateWeek = prepare.CreateWeekFactory.get_c1_week(db, cycle_id=cycle_id)
    weeks_id: list[int] = create_week.create()
    logging.info("Create c1 weeks")

    create_day: CreateMovableDay = prepare.CreateMovableDayFactory.get_c1_day(db, weeks_id=weeks_id)
    days_id: list[int] = create_day.create()
    logging.info("Create c1 days")

    crud.create_movable_date(
        db,
        movable_day_id=1,
        divine_service_title=enums.DivineServiceTitle.vespers,
        movable_date=schemas.MovableDateCreate()
    )
    create_movable_date: CreateMovableDate = prepare.CreateMovableDateFactory.get_c1_movable_date(db, days_id=days_id)
    movable_dates_id: list[int] = create_movable_date.create()
    logging.info("Create c1 movable dates")


def create_all_c2_movable_dates(db: Session):
    cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_2).id

    create_week: CreateWeek = prepare.CreateWeekFactory.get_c2_week(db, cycle_id=cycle_id)
    weeks_id: list[int] = create_week.create()
    logging.info("Create c2 weeks")

    create_day: CreateMovableDay = prepare.CreateMovableDayFactory.get_c2_day(db, weeks_id=weeks_id)
    days_id: list[int] = create_day.create()
    logging.info("Create c2 days")

    create_movable_date: CreateMovableDate = prepare.CreateMovableDateFactory.get_c2_movable_date(db, days_id=days_id)
    movable_dates_id: list[int] = create_movable_date.create()
    logging.info("Create c2 movable dates")


def create_all_c3_movable_dates(db: Session):
    cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_3).id

    create_week: CreateWeek = prepare.CreateWeekFactory.get_c3_week(db, cycle_id=cycle_id)
    weeks_id: list[int] = create_week.create()
    logging.info("Create c3 weeks")

    create_day: CreateMovableDay = prepare.CreateMovableDayFactory.get_c3_day(db, weeks_id=weeks_id)
    days_id: list[int] = create_day.create()
    logging.info("Create c3 days")

    # create_movable_date: CreateMovableDate = prepare.CreateMovableDateFactory.get_c3_movable_date(db, days_id=days_id)
    # movable_dates_id: list[int] = create_movable_date.create()
    # logging.info("Create c3 movable dates")


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    Base.metadata.create_all(bind=engine)
    create_all_movable_dates(db)
 