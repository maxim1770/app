from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud, enums
from app.create.create.base_cls import FatalCreateError


def create_bible_books(db: Session) -> bool:
    """
     Создает 27 = 4 + 23 записи об Книгах Нового Завета в таблице `bible_books`.

    **Все данные введены вручную, не из парсера.**

     :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
     """
    number_bible_books: Final[int] = 4 + 23

    # Над всеми bible_books.title еще нужно подумать, особенно про те, которые начинаются на '1/2-е послание ...'
    bible_books: list[schemas.BibleBookEvangelCreate | schemas.BibleBookApostleCreate] = [
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Матфея',
            abbr=enums.BibleBookAbbr.Mt
        ),
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Марка',
            abbr=enums.BibleBookAbbr.Mk
        ),
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Луки',
            abbr=enums.BibleBookAbbr.Lk
        ),
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Иоанна',
            abbr=enums.BibleBookAbbr.Jn
        ),

        # Деяния святых Апостолов
        schemas.BibleBookApostleCreate(
            title='Деяния святых Апостолов',
            abbr=enums.BibleBookAbbr.Act
        ),

        # Соборные Послания
        schemas.BibleBookApostleCreate(
            title='Послание Иакова',
            abbr=enums.BibleBookAbbr.Jac
        ),
        schemas.BibleBookApostleCreate(
            title='1-е послание Петра',
            abbr=enums.BibleBookAbbr._1Pet
        ),
        schemas.BibleBookApostleCreate(
            title='2-е послание Петра',
            abbr=enums.BibleBookAbbr._2Pet
        ),
        schemas.BibleBookApostleCreate(
            title='1-е послание Иоанна',
            abbr=enums.BibleBookAbbr._1Jn
        ),
        schemas.BibleBookApostleCreate(
            title='2-е послание Иоанна',
            abbr=enums.BibleBookAbbr._2Jn
        ),
        schemas.BibleBookApostleCreate(
            title='3-е послание Иоанна',
            abbr=enums.BibleBookAbbr._3Jn
        ),
        schemas.BibleBookApostleCreate(
            title='Послание Иуды',
            abbr=enums.BibleBookAbbr.Juda
        ),

        # Послания Апостола Павла
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Римлянам',
            abbr=enums.BibleBookAbbr.Rom
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 1-е послание к коринфянам',
            abbr=enums.BibleBookAbbr._1Cor
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 2-е послание к коринфянам',
            abbr=enums.BibleBookAbbr._2Cor
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Галатам',
            abbr=enums.BibleBookAbbr.Gal
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Ефесянам',
            abbr=enums.BibleBookAbbr.Eph
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Филиппийцам',
            abbr=enums.BibleBookAbbr.Phil
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Колоссянам',
            abbr=enums.BibleBookAbbr.Col
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 1-е послание к фессалоникийцам',
            abbr=enums.BibleBookAbbr._1Thes
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 2-е послание к фессалоникийцам',
            abbr=enums.BibleBookAbbr._2Thes
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 1-е послание к Тимофею',
            abbr=enums.BibleBookAbbr._1Tim
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 2-е послание к Тимофею',
            abbr=enums.BibleBookAbbr._2Tim
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Титу',
            abbr=enums.BibleBookAbbr.Tit
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла послание к Филимону',
            abbr=enums.BibleBookAbbr.Phlm
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Евреям',
            abbr=enums.BibleBookAbbr.Hebr
        ),

        # Апокалипсис
        schemas.BibleBookApostleCreate(
            title='Откровение Иоанна Богослова',
            abbr=enums.BibleBookAbbr.Apok
        ),
    ]

    num_creatures: int = 0

    for bible_book in bible_books:
        # TODO тут изменить аргументы get_bible_book, если все таки решу использовать только abbr
        if crud.get_bible_book(db, testament=bible_book.testament, part=bible_book.part, abbr=bible_book.abbr):
            raise FatalCreateError(
                f'BibleBook: testament={bible_book.testament}, part={bible_book.part}, abbr={bible_book.abbr} уже была создана')

        crud.create_bible_book(db, bible_book=bible_book)
        num_creatures += 1

    if number_bible_books != num_creatures:
        raise FatalCreateError(
            f'Не создались {number_bible_books} записи об книгах Нового Завета в таблице `bible_books`.')
    return True
