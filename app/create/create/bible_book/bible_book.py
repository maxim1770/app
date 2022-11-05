from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


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
            abbr=schemas.AbbrEnum.Mt
        ),
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Марка',
            abbr=schemas.AbbrEnum.Mk
        ),
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Луки',
            abbr=schemas.AbbrEnum.Lk
        ),
        schemas.BibleBookEvangelCreate(
            title='Евангелие от Иоанна',
            abbr=schemas.AbbrEnum.Jn
        ),

        # Деяния святых Апостолов
        schemas.BibleBookApostleCreate(
            title='Деяния святых Апостолов',
            abbr=schemas.AbbrEnum.Act
        ),

        # Соборные Послания
        schemas.BibleBookApostleCreate(
            title='Послание Иакова',
            abbr=schemas.AbbrEnum.Jac
        ),
        schemas.BibleBookApostleCreate(
            title='1-е послание Петра',
            abbr=schemas.AbbrEnum._1Pet
        ),
        schemas.BibleBookApostleCreate(
            title='2-е послание Петра',
            abbr=schemas.AbbrEnum._2Pet
        ),
        schemas.BibleBookApostleCreate(
            title='1-е послание Иоанна',
            abbr=schemas.AbbrEnum._1Jn
        ),
        schemas.BibleBookApostleCreate(
            title='2-е послание Иоанна',
            abbr=schemas.AbbrEnum._2Jn
        ),
        schemas.BibleBookApostleCreate(
            title='3-е послание Иоанна',
            abbr=schemas.AbbrEnum._3Jn
        ),
        schemas.BibleBookApostleCreate(
            title='Послание Иуды',
            abbr=schemas.AbbrEnum.Juda
        ),

        # Послания Апостола Павла
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Римлянам',
            abbr=schemas.AbbrEnum.Rom
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 1-е послание к коринфянам',
            abbr=schemas.AbbrEnum._1Cor
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 2-е послание к коринфянам',
            abbr=schemas.AbbrEnum._2Cor
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Галатам',
            abbr=schemas.AbbrEnum.Gal
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Ефесянам',
            abbr=schemas.AbbrEnum.Eph
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Филиппийцам',
            abbr=schemas.AbbrEnum.Phil
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Колоссянам',
            abbr=schemas.AbbrEnum.Col
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 1-е послание к фессалоникийцам',
            abbr=schemas.AbbrEnum._1Thes
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 2-е послание к фессалоникийцам',
            abbr=schemas.AbbrEnum._2Thes
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 1-е послание к Тимофею',
            abbr=schemas.AbbrEnum._1Tim
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла 2-е послание к Тимофею',
            abbr=schemas.AbbrEnum._2Tim
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Титу',
            abbr=schemas.AbbrEnum.Tit
        ),
        schemas.BibleBookApostleCreate(
            title='Апостола Павла послание к Филимону',
            abbr=schemas.AbbrEnum.Phlm
        ),
        schemas.BibleBookApostleCreate(
            title='Послание апостола Павла к Евреям',
            abbr=schemas.AbbrEnum.Hebr
        ),

        # Апокалипсис
        schemas.BibleBookApostleCreate(
            title='Откровение Иоанна Богослова',
            abbr=schemas.AbbrEnum.Apok
        ),
    ]

    number_creatures: int = 0

    for bible_book in bible_books:
        # TODO тут изменить аргументы get_bible_book, если все таки решу использовать только abbr
        if crud.get_bible_book(db, testament=bible_book.testament, part=bible_book.part, abbr=bible_book.abbr):
            raise ValueError(
                f'BibleBook: testament={bible_book.testament}, part={bible_book.part}, abbr={bible_book.abbr} уже была создана')

        crud.create_bible_book(db, bible_book=bible_book)
        number_creatures += 1

    if number_bible_books != number_creatures:
        raise ValueError(
            f'Не создались {number_bible_books} записи об книгах Нового Завета в таблице `bible_books`.')
    return True
