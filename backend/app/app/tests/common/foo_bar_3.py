from sqlalchemy.orm import Session

from app import crud
from app.api import deps

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    book_id = crud.book.get_random_topic_book_id(db)
    print(book_id)
