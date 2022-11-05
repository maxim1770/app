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

    num_creatures: int = 0

    for bible_book_abbr, zachalo in zip(bible_books_abbrs, zachalos):

        if crud.get_zachalo(db, bible_book_abbr=bible_book_abbr, num=zachalo.num):
            raise ValueError(
                f'Zachalo: bible_book_abbr={bible_book_abbr}, num={zachalo.num} уже была создана')

        crud.create_zachalo(db, bible_book_abbr=bible_book_abbr, zachalo=zachalo)
        num_creatures += 1

        print_view: str = 'Apostole' if num_creatures % 2 == 0 else 'Evangel'
        print(f'(+)', num_creatures, "|", {print_view}, "|", zachalo.num, "|", bible_book_abbr)

    if number_zachalos != num_creatures:
        raise ValueError(
            f'Не создались {number_zachalos} записи об зачалах в таблице `zachalos`.')
    return True
