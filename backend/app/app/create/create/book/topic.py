from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import FatalCreateError


def create_all_topics(db: Session) -> None:
    if crud.topic.get_all(db):
        raise FatalCreateError(f'Topic: topics already created')
    topics_in = [
        schemas.TopicCreate(title=book_topic)
        for book_topic in enums.BookTopic
    ]
    for topic_in in topics_in:
        crud.topic.create(db, obj_in=topic_in)
