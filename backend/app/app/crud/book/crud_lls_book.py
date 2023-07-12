from sqlalchemy.orm import Session

from app import models, schemas


def create_lls_book(
        db: Session,
        *,
        id: int,
        lls_book_in: schemas.LlsBookCreate,
        year_id: int,
) -> models.LlsBook:
    db_lls_book = models.LlsBook(
        id=id,
        **lls_book_in.model_dump(),
        year_id=year_id
    )
    db.add(db_lls_book)
    db.commit()
    db.refresh(db_lls_book)
    return db_lls_book
