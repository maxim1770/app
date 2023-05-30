from sqlalchemy.orm import Session

from app import schemas, crud, enums
from .base_cls import FatalCreateError


def create_all_cities(db: Session) -> None:
    if crud.get_cities(db):
        raise FatalCreateError(f'City: cities уже были созданы')
    cities_in = [schemas.CityCreate(title=city_title) for city_title in enums.CityTitle]
    for city_in in cities_in:
        crud.create_city(db, city_in=city_in)
