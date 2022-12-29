import logging

logging.basicConfig(  # filename="create.log", filemode="w", encoding='utf-8',
    format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps


def print_table_reading(db: Session):
    cycle_1 = crud.get_cycle(db, num=schemas.CycleEnum.cycle_1)
    for week in cycle_1.weeks:

        print(f'Неделя {week.sunday_num}')

        for day in week.days:
            movable_dates = day.movable_dates
            movable_date_liturgy = [movable_date for movable_date in movable_dates
                                    if movable_date.divine_service.title == schemas.DivineServiceEnum.liturgy
                                    ][0]
            readings = movable_date_liturgy.readings
            reading_apostle = [reading for reading in readings
                               if reading.zachalo.bible_book_id > 4
                               ][0]

            zachalo = reading_apostle.zachalo
            bible_book = zachalo.bible_book

            # if bible_book.id <= 4:
            print(f'{day.abbr_ru} | {bible_book.abbr_ru} - {zachalo.num}')


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    print_table_reading(db)
