import logging

from sqlalchemy.orm import Session

from app.api import deps
from app.create import prepare
from app.create.create.bible_book.bible_book import create_bible_books
from app.create.create.bible_book.zachalo import CreateZachalo
from app.db.session import engine, Base


def create_all_zachalos(db: Session):
    create_bible_books(db)
    # logging.info("Create bible books")

    # zachalos_id: list[int] = create_all_c1_zachalos(db)

    # zachalos_id: list[int] = create_all_c2_zachalos(db)


def create_all_c1_zachalos(db: Session) -> list[int]:
    create_zachalo: CreateZachalo = prepare.CreateZachaloFactory.get_c1_zachalo(db)
    zachalos_id: list[int] = create_zachalo.create()
    logging.info("Create c1 zachalos")

    return zachalos_id


def create_all_c2_zachalos(db: Session) -> list[int]:
    create_zachalo: CreateZachalo = prepare.CreateZachaloFactory.get_c2_zachalo(db)
    zachalos_id: list[int] = create_zachalo.create()
    logging.info("Create c2 zachalos")

    return zachalos_id


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    Base.metadata.create_all(bind=engine)
    create_all_zachalos(db)
