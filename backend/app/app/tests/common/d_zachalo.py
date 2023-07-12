import csv
import logging

from app import crud
from app.api import deps

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == '__main__':
    db = next(deps.get_db())
    # create.create_all_movable_dates(db)
    # create.create_all_zachalos_movable_dates_associations(db)
    # create.create_dates_for_years(db)

    with open(r"C:\Users\MaxDroN\Downloads\data-1689069817174.csv", encoding='utf-8') as r_file:
        reader_object = csv.reader(r_file, delimiter=",")
        for row in list(reader_object)[1:]:
            saint_id, holiday_id = map(int, row)
            logging.info(saint_id)
            logging.info(holiday_id)
            logging.info('- - -')

            holiday = crud.holiday.get(db, id=holiday_id)
            saint = crud.saint.get(db, id=saint_id)
            crud.holiday.create_saint_association(db, db_obj=holiday, saint=saint)
