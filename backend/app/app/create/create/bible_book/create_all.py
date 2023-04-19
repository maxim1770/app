import logging

from sqlalchemy.orm import Session

from .bible_book import create_bible_books
from .zachalos_movable_dates import CreateZachaloMovableDateAssociationFactory


def create_all_bible_books(db: Session):
    create_bible_books(db)
    logging.info('Created Bible Books')


def create_c1_zachalos_movable_dates_associations(db: Session):
    create_zachalo_movable_date_association = CreateZachaloMovableDateAssociationFactory.get_c1(db)
    zachalos_id: list[int] = create_zachalo_movable_date_association.create()
    logging.info('Created c1 zachalos movable dates associations')


def create_c2_zachalos_movable_dates_associations(db: Session):
    create_zachalo_movable_date_association = CreateZachaloMovableDateAssociationFactory.get_c2(db)
    zachalos_id: list[int] = create_zachalo_movable_date_association.create()
    logging.info('Created c2 zachalos movable dates associations')
