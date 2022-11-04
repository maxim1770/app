from bs4.element import Tag
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps

from app.db.session import engine, Base
from app.create import prepare, combine, const
from app.create.create.movable_date.cycle import create_cycles
from app.create.create.movable_date.week import create_weeks
from app.create.create.movable_date.day import create_days
from app.create.create.movable_date.divine_service import create_divine_services
from app.create.create.movable_date.movable_date import create_movable_dates


def create_all_movable_dates(db: Session):
    print('create_cycles', create_cycles(db))
    print('create_divine_services', create_divine_services(db))

    print("c1")
    create_all_c_1_movable_dates(db)

    print("c2")

    create_all_c_2_movable_dates(db)


def create_all_c_1_movable_dates(db: Session):
    weeks: list[schemas.WeekCreate] = combine.combine_fields_for_weeks(**prepare.get_fields_for_c1_weeks())

    days: list[schemas.DayCreate] = combine.combine_fields_for_days(**prepare.get_fields_for_c1_days())

    print('create_weeks',
          create_weeks(db, cycle_num=schemas.CycleEnum.cycle_1, weeks=weeks, number_weeks=const.NumSunday.IN_CYCLE_1))
    sundays_nums: list[int] = [week.sunday_num for week in weeks]
    print('create_days', create_days(db,
                                     cycle_num=schemas.CycleEnum.cycle_1,
                                     sundays_nums=sundays_nums,
                                     days=days,
                                     number_days=const.NumWeek.IN_CYCLE_1 * 7
                                     )
          )

    table: Tag = prepare.collect_table()
    prepare_sunday_matins: prepare.PrepareSundayMatins = prepare.PrepareSundayMatins(table=table)
    sundays_matins: list[int | None] = prepare.PrepareC1SundayMatins(prepare_sunday_matins.data.copy()).data

    sundays_vespers: list[bool] = prepare.PrepareC1SundayVespers().data

    days_abbrs: list[schemas.DayAbbrEnum] = [day.abbr for day in days]
    print('create_movable_dates',
          create_movable_dates(db,
                               cycle_num=schemas.CycleEnum.cycle_1,
                               sundays_nums=sundays_nums,
                               days_abbrs=days_abbrs,
                               sundays_matins=sundays_matins,
                               sundays_vespers=sundays_vespers,
                               number_movable_dates=const.NumWeek.IN_CYCLE_1 * 7 + (const.NumSunday.IN_CYCLE_1 - 1) + 1
                               )
          )


def create_all_c_2_movable_dates(db: Session):
    weeks: list[schemas.WeekCreate] = combine.combine_fields_for_weeks(**prepare.get_fields_for_c2_weeks())
    print('create_weeks',
          create_weeks(db, cycle_num=schemas.CycleEnum.cycle_2, weeks=weeks, number_weeks=const.NumSunday.IN_CYCLE_2))

    days: list[schemas.DayCreate] = combine.combine_fields_for_days(**prepare.get_fields_for_c2_days())

    sundays_nums: list[int] = [week.sunday_num for week in weeks]
    print('create_days', create_days(db,
                                     cycle_num=schemas.CycleEnum.cycle_2,
                                     sundays_nums=sundays_nums,
                                     days=days,
                                     # + 1 потому что в 36 недели есть только Воскресение
                                     number_days=(const.NumWeek.IN_CYCLE_2 * 7) + 1
                                     )
          )

    table: Tag = prepare.collect_table()
    prepare_sunday_matins: prepare.PrepareSundayMatins = prepare.PrepareSundayMatins(table=table)
    sundays_matins: list[int] = prepare.PrepareC2SundayMatins(prepare_sunday_matins.data.copy()).data

    sundays_vespers: list[False] = [False] * const.NumSunday.IN_CYCLE_2

    days_abbrs: list[schemas.DayAbbrEnum] = [day.abbr for day in days]

    print('create_movable_dates',
          create_movable_dates(db,
                               cycle_num=schemas.CycleEnum.cycle_2,
                               sundays_nums=sundays_nums,
                               days_abbrs=days_abbrs,
                               sundays_matins=sundays_matins,
                               sundays_vespers=sundays_vespers,
                               number_movable_dates=const.NumWeek.IN_CYCLE_2 * 6 + const.NumSunday.IN_CYCLE_2 * 2
                               )
          )

    # TODO создать базовый класс по аналогии с Prepare


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    Base.metadata.create_all(bind=engine)
    create_all_movable_dates(db)
