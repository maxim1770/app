from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud
from app.create.create.base_cls import FatalCreateError


def create_divine_services(db: Session) -> bool:
    """
    Создает 3 Божественные службы в таблице "divine_services".

    **Все данные введены вручную, не из парсера.**

    :return: true, если все создалось успешно. Или завершается с ошибкой ValueError.
    """
    number_divine_services: Final[int] = 3

    divine_services: list[schemas.DivineServiceCreate] = [
        schemas.DivineServiceCreate(
            title=schemas.DivineServiceEnum.matins,
        ),
        schemas.DivineServiceCreate(
            title=schemas.DivineServiceEnum.liturgy,
        ),
        schemas.DivineServiceCreate(
            title=schemas.DivineServiceEnum.vespers,
        )
    ]

    num_creatures: int = 0

    for divine_service in divine_services:
        if crud.get_divine_service(db, title=divine_service.title):
            raise FatalCreateError(
                f'DivineService: title={divine_service.title} уже была создана')

        crud.create_divine_service(db, divine_service=divine_service)
        num_creatures += 1

    if number_divine_services != num_creatures:
        raise FatalCreateError(
            f'Не создались {number_divine_services} записи о Божественных службах в таблице `divine_services`.')
    return True
