import logging

import sqlalchemy as sa

from app import models

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

from sqlalchemy.orm import Session
from app.api import deps


def delete_all_orphan_books(db: Session) -> None:
    num = 0
    for book in db.execute(sa.select(models.Book).filter(
            (models.Book.topic_book == None) &
            (models.Book.holiday_book == None) &
            (models.Book.molitva_book == None) &
            (models.Book.movable_date_book == None) &
            (models.Book.lls_book == None) &
            (models.Book.zachalo == None) &
            (models.Book.cathedral_book == None) &
            (models.Book.psaltyr_book == None)
    )).scalars().all():
        if book.bookmarks:
            continue
        logging.warning(f'{book.id}, {book.title}')
        num += 1
        # crud.book.remove(db, id=book.id)
    logging.warning('- - -')
    logging.warning(num)


def delete_all_orphan_pages() -> None:
    """
    SELECT *
    FROM page
    WHERE NOT EXISTS (
        SELECT 1
        FROM manuscript
        WHERE manuscript.preview_page_id = page.id
        OR EXISTS (
            SELECT 1
            FROM bookmark
            WHERE bookmark.first_page_id = page.id OR bookmark.end_page_id = page.id
        )
    );
    """
    # Вот такой запрос в консоль в DataGrip, после выполнения нажимаем All отобразить строк
    # и ctrl + A удаляем все строки таблицы ( "-" сверху на панели задач)


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    # delete_all_orphan_books(db)
