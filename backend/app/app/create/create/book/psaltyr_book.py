from typing import Final

from sqlalchemy.orm import Session

from app import crud, enums, schemas, models


def create_all_psaltyr_books(db: Session) -> None:
    num_psalom: Final[int] = 150
    for psaltyr_num in range(1, num_psalom + 1):
        psaltyr_book_in = schemas.PsaltyrBookCreate(num=psaltyr_num)
        psaltyr_book: models.PsaltyrBook = crud.create_psaltyr_book(
            db,
            bible_book_abbr=enums.BibleBookAbbr.Ps,
            psaltyr_book_in=psaltyr_book_in
        )
        crud.create_psaltyr_book_tolkovoe(db, psaltyr_book=psaltyr_book)
