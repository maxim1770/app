from sqlalchemy.orm import Session

from app.api import deps
from app.create.create.book.topic import create_all_topics

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    create_all_topics(db)
