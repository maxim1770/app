import logging

from app import crud

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

from sqlalchemy.orm import Session
from app.api import deps


def delete_all_orphan_years(db: Session) -> None:
    """
    Или так

    SELECT *
    FROM year
    WHERE NOT EXISTS (SELECT 1
                      FROM manuscript
                      WHERE manuscript.year_id = year.id
                         OR EXISTS (SELECT 1
                                    FROM holiday
                                    WHERE holiday.year_id = year.id)
                         OR EXISTS (SELECT 1
                                    FROM icon
                                    WHERE icon.year_id = year.id)
                         OR EXISTS (SELECT 1
                                    FROM cathedral
                                    WHERE cathedral.year_id = year.id)
                         OR EXISTS (SELECT 1
                                    FROM lls_book
                                    WHERE lls_book.year_id = year.id));

    Вот такой запрос в консоль в DataGrip, после выполнения нажимаем All отобразить строк
    и ctrl + A удаляем все строки таблицы ( "-" сверху на панели задач)
    """

    num = 0
    for year in crud.year.get_all(db):
        if year.manuscripts or year.holidays or year.icons or year.cathedrals or year.lls_books:
            continue
        logging.warning(f'{year.id}, {year.title}')
        num += 1
        # crud.year.remove(db, id=year.id)
    logging.warning('- - -')
    logging.warning(num)


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    delete_all_orphan_years(db)
