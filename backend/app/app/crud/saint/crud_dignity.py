from pydantic import BaseModel

from app.models import Dignity
from app.schemas import DignityCreate, DignityUpdate
from ..base import CRUDBase


class DignityFilter(BaseModel):
    pass


class CRUDDignity(CRUDBase[Dignity, DignityCreate, DignityUpdate, DignityFilter]):
    pass


dignity = CRUDDignity(Dignity)
