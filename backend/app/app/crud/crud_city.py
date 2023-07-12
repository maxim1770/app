from pydantic import BaseModel

from app.models import City
from app.schemas import CityCreate, CityUpdate
from .base import CRUDBase


class CityFilter(BaseModel):
    pass


class CRUDCity(CRUDBase[City, CityCreate, CityUpdate, CityFilter]):
    pass


city = CRUDCity(City)
