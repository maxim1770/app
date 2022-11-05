from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.create import prepare, combine, const
from app.create.create.reading import create_readings

from app.create.create.movable_date.create_all import create_all_movable_dates


def create_all(db: Session):
    # create_all_movable_dates(db)

    print('c1')
    create_c1_readings(db)


def create_c1_readings(db: Session):
    weeks: list[schemas.WeekCreate] = combine.combine_fields_weeks(**prepare.prepare_fields_c1_weeks())

    sundays_nums: list[int] = [week.sunday_num for week in weeks]

    days: list[schemas.DayCreate] = combine.combine_fields_days(**prepare.prepare_fields_c1_days())

    days_abbrs: list[schemas.DayAbbrEnum] = [day.abbr for day in days]

    zachalos: list[schemas.ZachaloCreate] = combine.combine_fields_zachalos(**prepare.prepare_fields_c1_zachalos())

    zachalos_nums: list[int] = [zachalo.num for zachalo in zachalos]

    bible_books_abbrs: list[schemas.AbbrEnum] = prepare.prepare_с1_bible_books_abbrs()

    print('create_readings', create_readings(db,
                                             cycle_num=schemas.CycleEnum.cycle_1,
                                             sundays_nums=sundays_nums,
                                             days_abbrs=days_abbrs,
                                             bible_books_abbrs=bible_books_abbrs,
                                             zachalos_nums=zachalos_nums,
                                             number_readings= const.NumWeek.IN_CYCLE_1 * 7 * 2
                                             )
          )


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    create_all(db)
