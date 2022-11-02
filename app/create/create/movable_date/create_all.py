from bs4.element import Tag
from sqlalchemy.orm import Session

from app.create import prepare, combine
from app.create.create.movable_date.cycle import create_cycles
from app.create.create.movable_date.week import create_c1_weeks
from app.create.create.movable_date.day import create_c1_days
from app.create.create.movable_date.divine_service import create_divine_services
from app.create.create.movable_date.movable_date import create_c1_movable_dates
from app.api import deps
from app import schemas


def create_all_movable_dates(db: Session):
    print(create_cycles(db))
    create_all_c_1_movable_dates(db)


def create_all_c_1_movable_dates(db: Session):
    c1_weeks: list[schemas.WeekCreate] = combine.combine_fields_for_c1_weeks()

    c1_days: list[schemas.DayCreate] = combine.combine_fields_for_c1_days()

    print(create_c1_weeks(db, c1_weeks=c1_weeks))
    c1_sundays_nums: list[int] = [week.sunday_num for week in c1_weeks]
    print(create_c1_days(db,
                         c1_sundays_nums=c1_sundays_nums,
                         c1_days=c1_days))

    table: Tag = prepare.collect_table()
    prepare_sunday_matins: prepare.PrepareSundayMatins = prepare.PrepareSundayMatins(table=table)
    is_c1_sundays_matins: list[bool] = prepare.PrepareС1SundayMatins(prepare_sunday_matins.data.copy()).data

    is_c1_sundays_vespers: list[bool] = prepare.PrepareС1SundayVespers().data

    print(create_divine_services(db))

    c1_days_abbrs: list[schemas.DayAbbrEnum] = [day.abbr for day in c1_days]
    print(
        create_c1_movable_dates(db,
                                c1_sundays_nums=c1_sundays_nums,
                                c1_days_abbrs=c1_days_abbrs,
                                is_c1_sundays_matins=is_c1_sundays_matins,
                                is_c1_sundays_vespers=is_c1_sundays_vespers
                                )
    )


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    create_all_movable_dates(db)
