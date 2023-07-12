from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import FatalCreateError


def create_bible_books(db: Session) -> None:
    """Над всеми bible_books.title еще нужно подумать, особенно про те, которые начинаются на '1/2-е послание ...'"""
    bible_books: list[
        schemas.BibleBookEvangelCreate | schemas.BibleBookApostleCreate | schemas.BibleBookPsaltyrCreate] = [
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

        schemas.BibleBookPsaltyrCreate(
            title='Псалтырь',
            abbr=enums.BibleBookAbbr.Ps
        ),

        schemas.BibleBookPjatiknizhieMoisejaCreate(
            title='Бытие́',
            abbr=enums.BibleBookAbbr.Gen
        ),
        schemas.BibleBookPjatiknizhieMoisejaCreate(
            title='Исхо́д',
            abbr=enums.BibleBookAbbr.Ex
        ),
        schemas.BibleBookPjatiknizhieMoisejaCreate(
            title='Леви́т',
            abbr=enums.BibleBookAbbr.Lev
        ),
        schemas.BibleBookPjatiknizhieMoisejaCreate(
            title='Числа́',
            abbr=enums.BibleBookAbbr.Num
        ),
        schemas.BibleBookPjatiknizhieMoisejaCreate(
            title='Второзако́ние',
            abbr=enums.BibleBookAbbr.Deut
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Книга Исуса Навгина',
            abbr=enums.BibleBookAbbr.Nav
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Книга Судей Израилевых',
            abbr=enums.BibleBookAbbr.Judg
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Книга Руфь',
            abbr=enums.BibleBookAbbr.Rth
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Царство первое',
            abbr=enums.BibleBookAbbr._1Sam
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Царство второе',
            abbr=enums.BibleBookAbbr._2Sam
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Царство третье',
            abbr=enums.BibleBookAbbr._1King
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Царство четвертое',
            abbr=enums.BibleBookAbbr._2King
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Царство четвертое',
            abbr=enums.BibleBookAbbr._2King
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Царство четвертое',
            abbr=enums.BibleBookAbbr._2King
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Книга глаголемая Товия',
            abbr=enums.BibleBookAbbr.Tov
        ),
        schemas.BibleBookOldTestamentCreate(
            title='Книга Есфирь',
            abbr=enums.BibleBookAbbr.Est
        ),
    ]
    for bible_book in bible_books:
        if crud.get_bible_book(db, abbr=bible_book.abbr):
            raise FatalCreateError(f'BibleBook: abbr={bible_book.abbr} already created')
        crud.create_bible_book(db, bible_book=bible_book)
