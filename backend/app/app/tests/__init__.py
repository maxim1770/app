import logging

import sqlalchemy as sa
from app import models, enums
from app.api import deps
from app.create.create.bible_book.create_all import create_c1_zachalos_movable_dates_associations, create_c2_zachalos_movable_dates_associations,create_bible_books

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    db = next(deps.get_db())
    # create_bible_books(db)
    # create_c1_zachalos_movable_dates_associations(db)
    # create_c2_zachalos_movable_dates_associations(db)


    objs = db.execute(sa.select(models.Zachalo).join(models.BibleBook).filter(models.BibleBook.abbr=enums.BibleBookAbbr.Act)).
    # db.delete(objs)
    # db.commit()
    print(objs)