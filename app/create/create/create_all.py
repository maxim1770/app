import logging

from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps
from app.create import const
from app.create.create.bible_book.create_all import create_all_c1_zachalos
from app.create.create.reading import CreateReading
from app.db.session import engine, Base


# TODO
#  изменить названия с классами Enum и убрать слово Enum, заменить на названия таблицы + поле
#  подумать над тем чтобы не создавать schemas в ф. create_c1_readings, а написать функции в модулях prepare
#  которые будут сразу выдавать нужные значения


# TODO: возможно переписать try: except в бизнес логике, т.к это штатная ситуация, а мы ее пишем как исключение
#  так же создать два класса исключений ожидаемых, и не ожидаемых, и из использовать вместо исключений python
#  т.к если использовать наследование от python исключений, то оно может вызваться от безобидной функции

# TODO: переимновать классы Prepare...Factory на что-то другое, т.к иногда они возвращают вообще не класс, а список данных
#  + возможно стоит переделать все эти классы, чтобы они возвращали список, но это спорно
#  тут стоит смотреть на то, использует ли класс Create...Factory, что-то кроме .data класса Prepare...Factory
#  если только data в большинстве классах, то все переделать так, чтобы возвращались списки данных,
#  а не классы Prepare... из Prepare...Factory


# TODO: сделать декоратор из функции convert_to_schemas(), думаю будет достаточно декоратора функции, класс декоратор не нужен
# TODO: Возможно где-то добавить проверку на равенсто списков, которые нужны для создания схем,
#  возможно это можно сделать в декораторе, но не знаю насколько это верно
#  да и + к тому же эта проверка не всегда нужна, т.к часто все классы наследуются от общено и списки точно равны межуд собой
#  ХОЯТ ДАЖЕ В ТАКОЙ СИТУАЦИ НЕ ТОЧНО, Т.К МЫ МОЖЕТ ПЕРЕОПРЕДЕЛИТЬ self.data ВНУТРИ КЛАССА
#  так что где-то нужно делать проверку на равенство длин списков
#  и пусть эта проверка бросает исключение класс который мы создали, с критической ошибкой
#  хотя тоже спорный момент, т.к стоит помнить что это внутренний код,
#  и ошибка произошла только по моей криворукости скоре всего


def create_all(db: Session):
    zachalos_id: list[int] = create_all_c1_zachalos(db)

    create_c1_readings(db, zachalos_id)


class CreateReadingFactory(object):

    @staticmethod
    def get_c1_reading(db: Session, zachalos_id: list[int]) -> CreateReading:
        cycle_id: int = crud.get_cycle(db, num=schemas.CycleEnum.cycle_1).id
        divine_service_id: int = crud.get_divine_service(db, title=schemas.DivineServiceEnum.liturgy).id

        movable_dates_id: list[int] = [movable_date.id for movable_date in
                                       crud.get_movable_dates(db, cycle_id=cycle_id,
                                                              divine_service_id=divine_service_id)
                                       ]

        return CreateReading(
            db,
            parents_id=movable_dates_id,
            zachalos_id=zachalos_id,
            num_creatures=const.NumWeek.IN_CYCLE_1 * 7 * 2
        )


def create_c1_readings(db: Session, zachalos_id: list[int]):
    create_reading: CreateReading = CreateReadingFactory.get_c1_reading(db, zachalos_id=zachalos_id)
    readings_id: list[int] = create_reading.create()
    logging.info("Create c1 readings")


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    Base.metadata.create_all(bind=engine)
    create_all(db)
