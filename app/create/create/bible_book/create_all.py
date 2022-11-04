from sqlalchemy.orm import Session

from app.api import deps
from app.create.create.bible_book.bible_book import create_bible_books


def create_all_bible_books(db: Session):
    print(create_bible_books(db))


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    create_all_bible_books(db)
