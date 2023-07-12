from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import FatalCreateError


def create_all_faces_sanctity(db: Session) -> bool:
    number_faces_sanctity: Final[int] = 31

    num_creatures: int = 0

    for face_sanctity_title in enums.FaceSanctityTitle:
        if crud.face_sanctity.get_by_title(db, title=face_sanctity_title):
            raise FatalCreateError(f'FaceSanctity: title={face_sanctity_title} already created')

        crud.face_sanctity.create(db,
                                  obj_in=schemas.FaceSanctityCreate(
                                      title=face_sanctity_title
                                  )
                                  )
        num_creatures += 1

    if number_faces_sanctity != num_creatures:
        raise FatalCreateError(
            f'Не создались {number_faces_sanctity} записи FaceSanctity')
    return True
