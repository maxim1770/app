from sqlalchemy.orm import Session

from app.filters import TopicFilter
from app.models import Topic
from app.schemas import TopicCreate, TopicUpdate
from ..base import CRUDBase
from ... import models


class CRUDTopic(CRUDBase[Topic, TopicCreate, TopicUpdate, TopicFilter]):

    @staticmethod
    def create_topic_book_association(
            db: Session,
            *,
            db_obj: Topic,
            topic_book: models.TopicBook,
    ) -> Topic:
        db_obj.topic_book_associations.append(models.TopicBookTopicAssociation(topic_book=topic_book))
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


topic = CRUDTopic(Topic)
