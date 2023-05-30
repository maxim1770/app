from sqlalchemy.orm import Session

from app import models, schemas


def create_molitva_book(
        db: Session,
        *,
        id: int,
        molitva_book_in: schemas.MolitvaBookCreate,
        holiday_id: int,
) -> models.MolitvaBook:
    db_molitva_book = models.MolitvaBook(
        id=id,
        **molitva_book_in.dict(),
        holiday_id=holiday_id
    )
    db.add(db_molitva_book)
    db.commit()
    db.refresh(db_molitva_book)
    return db_molitva_book
