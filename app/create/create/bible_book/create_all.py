from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.create.create.bible_book.bible_book import create_bible_books
from app.create.create.bible_book.zachalo import create_zachalos
from app.db.session import engine, Base
from app.create import prepare, combine, const


def create_all_zachalos(db: Session):
    print('create_bible_books', create_bible_books(db))

    print('c1')
    create_all_c1_zachalos(db)


def create_all_c1_zachalos(db: Session):
    zachalos: list[schemas.ZachaloCreate] = combine.combine_fields_zachalos(**prepare.prepare_fields_c1_zachalos())

    bible_books_abbrs: list[schemas.AbbrEnum] = prepare.prepare_с1_bible_books_abbrs()

    print('create_zachalos', create_zachalos(db,
                                             bible_books_abbrs=bible_books_abbrs,
                                             zachalos=zachalos,
                                             number_zachalos=(const.NumWeek.IN_CYCLE_1 * 7) * 2
                                             )
          )


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()

    Base.metadata.create_all(bind=engine)

    create_all_zachalos(db)
