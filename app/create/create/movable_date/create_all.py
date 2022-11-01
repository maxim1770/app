from bs4.element import Tag
from sqlalchemy.orm import Session

from app.create import prepare
from app.create.create.movable_date.cycle import create_cycles
from app.create.create.movable_date.week import create_c1_weeks
from app.create.create.movable_date.day import create_c1_days
from app.create.create.movable_date.divine_service import create_divine_services
from app.create.create.movable_date.movable_date import create_c1_movable_dates
from app.api import deps
from app import schemas


def create_all():
    db: Session = deps.get_db().__next__()

    table: Tag = prepare.collect_table()

    sundays: list[str] = prepare.PrepareSunday(table=table).data
    c1_sundays: list[str] = prepare.PrepareС1Sunday(sundays).data
    c1_sundays_nums: list[int] = prepare.PrepareС1SundayNum(c1_sundays.copy()).data
    c1_sundays_titles: list[str] = prepare.PrepareС1SundayTitle(c1_sundays.copy()).data

    weeks: list[str] = prepare.PrepareWeek(table=table).data
    c1_weeks: list[str] = prepare.PrepareС1Week(weeks).data
    c1_weeks_nums: list[int] = prepare.PrepareС1WeekNum(c1_weeks.copy()).data
    c1_weeks_titles: list[str] = prepare.PrepareС1WeekTitle(c1_weeks.copy()).data

    days: list[str] = prepare.PrepareDay(table=table).data
    c1_days: list[str] = prepare.PrepareС1Day(days).data
    c1_days_abbrs: list[schemas.DayAbbrEnum] = prepare.PrepareС1DayAbbr(c1_days.copy()).data
    c1_days_titles: list[str | None] = prepare.PrepareС1DayTitle(c1_days.copy()).data

    # print(create_cycles(db))
    # print(create_c1_weeks(db,
    #                       c1_sundays_nums=c1_sundays_nums,
    #                       c1_sundays_titles=c1_sundays_titles,
    #                       c1_weeks_nums=c1_weeks_nums,
    #                       c1_weeks_titles=c1_weeks_titles
    #                       )
    #       )
    #
    # print(create_c1_days(db,
    #                      c1_sundays_nums=c1_sundays_nums,
    #                      c1_days_abbrs=c1_days_abbrs,
    #                      c1_days_titles=c1_days_titles
    #                      )
    #       )

    matins: list[str] = prepare.PrepareSundayMatins(table=table).data
    is_c1_sundays_matins: list[bool] = prepare.PrepareС1SundayMatins(matins).data

    is_c1_sundays_vespers: list[bool] = prepare.PrepareС1SundayVespers().data

    # print(create_divine_services(db))

    print(
        create_c1_movable_dates(db,
                                c1_sundays_nums=c1_sundays_nums,
                                c1_days_abbrs=c1_days_abbrs,
                                is_c1_sundays_matins=is_c1_sundays_matins,
                                is_c1_sundays_vespers=is_c1_sundays_vespers
                                )
    )


if __name__ == '__main__':
    create_all()
