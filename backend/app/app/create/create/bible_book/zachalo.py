import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import schemas, crud, enums, models
from ..base_cls import CreateBase


class CreateZachalo(CreateBase):

    def __init__(self,
                 db: Session,
                 items: list[schemas.ZachaloCreate],
                 parents_id: list[enums.BibleBookAbbr],
                 num_creatures: int):
        super().__init__(db, items, parents_id, num_creatures)

    def create(self) -> list[int]:
        zachalos_id: list[int] = []
        for bible_book_abbr, zachalo in zip(self.parents_id, self.items):
            # if crud.get_zachalo(self.db, bible_book_abbr=bible_book_abbr, num=zachalo.num):
            #     raise FatalCreateError(self.get_except_text_created(bible_book_abbr, zachalo))
            zachalos_id.append(crud.create_zachalo(self.db, bible_book_abbr=bible_book_abbr, zachalo_in=zachalo).id)
        self.check_num_creatures(zachalos_id)
        return zachalos_id


def create_missing_evangels_zachalos(db: Session) -> None:
    evangels = db.execute(
        sa.select(models.BibleBook).filter_by(part='evangel').order_by(models.BibleBook.id)).scalars().all()
    for evangel in evangels:
        for zachalo_num in range(1, evangel.last_zachalo_num + 1):
            if crud.get_zachalo(db, bible_book_abbr=evangel.abbr, num=zachalo_num):
                continue
            zachalo: models.Zachalo = crud.create_zachalo(
                db,
                bible_book_abbr=evangel.abbr,
                zachalo_in=schemas.ZachaloCreate(num=zachalo_num)
            )
            zachalo_tolkovoe: models.Zachalo = crud.create_zachalo_tolkovoe(db, zachalo=zachalo)


def create_missing_apostles_zachalos(db: Session) -> None:
    apostles = db.execute(
        sa.select(models.BibleBook).filter_by(part='apostle').filter(
            models.BibleBook.last_zachalo_num != None).order_by(models.BibleBook.id)).scalars().all()
    for i, apostle in enumerate(apostles):
        first_zachalo_num = apostles[i - 1].last_zachalo_num + 1 if i != 0 else 1
        last_zachalo_num = apostle.last_zachalo_num
        for zachalo_num in range(first_zachalo_num, last_zachalo_num + 1):
            if crud.get_zachalo(db, bible_book_abbr=apostle.abbr, num=zachalo_num):
                continue
            zachalo: models.Zachalo = crud.create_zachalo(
                db,
                bible_book_abbr=apostle.abbr,
                zachalo_in=schemas.ZachaloCreate(num=zachalo_num)
            )
            zachalo_tolkovoe: models.Zachalo = crud.create_zachalo_tolkovoe(db, zachalo=zachalo)
