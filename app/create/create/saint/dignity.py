from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud, enums
from app.create.create.base_cls import FatalCreateError


def create_dignities(db: Session) -> bool:
    number_dignities: Final[int] = 20

    num_creatures: int = 0

    for dignity_title in enums.DignityTitle:
        if crud.get_dignity(db, title=dignity_title):
            raise FatalCreateError(f'Dignity: title={dignity_title} уже была создана')

        crud.create_dignity(db,
                            dignity=schemas.DignityCreate(
                                title=dignity_title
                            )
                            )
        num_creatures += 1

    if number_dignities != num_creatures:
        raise FatalCreateError(
            f'Не создались {number_dignities} записи Dignity')
    return True
