from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import FatalCreateError


def create_all_tipikons(db: Session) -> None:
    if crud.tipikon.get_all(db):
        raise FatalCreateError(f'Tipikon: tipikons already created')
    tipikons_in = [
        schemas.TipikonCreate(title=tipikon_title)
        for tipikon_title in enums.TipikonTitle
    ]
    for tipikon_in in tipikons_in:
        crud.tipikon.create(db, obj_in=tipikon_in)
