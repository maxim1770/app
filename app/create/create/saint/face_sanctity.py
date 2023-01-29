from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import FatalCreateError


def create_all_faces_sanctity(db: Session) -> bool:
    number_faces_sanctity: Final[int] = 31

    num_creatures: int = 0

    for face_sanctity_title in enums.FaceSanctityTitle:
        if crud.get_face_sanctity(db, title=face_sanctity_title):
            raise FatalCreateError(f'FaceSanctity: title={face_sanctity_title} уже была создана')

        crud.create_face_sanctity(db,
                                  face_sanctity=schemas.FaceSanctityCreate(
                                      title=face_sanctity_title
                                  )
                                  )
        num_creatures += 1

    if number_faces_sanctity != num_creatures:
        raise FatalCreateError(
            f'Не создались {number_faces_sanctity} записи FaceSanctity')
    return True
