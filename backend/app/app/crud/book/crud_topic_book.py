from sqlalchemy.orm import Session

from app import models, schemas


def create_topic_book(
        db: Session,
        *,
        id: int,
        topic_book_in: schemas.TopicBookCreate
) -> models.TopicBook:
    db_topic_book = models.TopicBook(
        id=id,
        **topic_book_in.dict()
    )
    db.add(db_topic_book)
    db.commit()
    db.refresh(db_topic_book)
    return db_topic_book
