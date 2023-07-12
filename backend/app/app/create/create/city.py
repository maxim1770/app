from sqlalchemy.orm import Session

from app import schemas, crud, enums
from .base_cls import FatalCreateError


def create_all_cities(db: Session) -> None:
    if crud.city.get_all(db):
        raise FatalCreateError(f'City: cities already created')
    cities_in = [schemas.CityCreate(title=city_title) for city_title in enums.CityTitle]
    for city_in in cities_in:
        crud.city.create(db, obj_in=city_in)
