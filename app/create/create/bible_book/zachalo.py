from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


def create_zachalos(db: Session,
                    bible_books_abbrs: list[schemas.AbbrEnum],
                    zachalos: list[schemas.ZachaloCreate],
                    number_zachalos: Final[int]
                    ) -> bool:
    """
    # КОММЕНТАРИЙ ОСТАЛСЯ ИЗ create_c1_zachalos
    Создает 110 = 8*7 + 8*7 - 2 (ПОКА ЧТО НЕ ПОЛУЧИЛОСЬ ДОБАВИТЬ ИХ) записи о Апостольских и Евангельских зачалах в таблице 'nums'.

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Большинство данных с парсера, но данные не надежны (номера зачал), возможны баги при получении данных с сайта azbyka.ru/biblia/...**

    :return: количество созданных записей в таблице.
    """

    number_creatures: int = 0

    for bible_book_abbr, zachalo in zip(bible_books_abbrs, zachalos):

        if crud.get_zachalo(db, bible_book_abbr=bible_book_abbr, num=zachalo.num):
            raise ValueError(
                f'Zachalo: bible_book_abbr={bible_book_abbr}, num={zachalo.num} уже была создана')

        crud.create_zachalo(db, bible_book_abbr=bible_book_abbr, zachalo=zachalo)
        number_creatures += 1

        print: str = 'Apostole' if number_creatures % 2 == 0 else 'Evangel'
        print(f'(+)', number_creatures, "|", {print}, "|", zachalo.num, "|", bible_book_abbr)

    if number_zachalos != number_creatures:
        raise ValueError(
            f'Не создались {number_zachalos} записи об зачалах в таблице `zachalos`.')
    return True
