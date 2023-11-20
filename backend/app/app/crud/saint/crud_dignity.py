from app.filters import DignityFilter
from app.models import Dignity
from app.schemas import DignityCreate, DignityUpdate

from ..base import CRUDBase


class CRUDDignity(CRUDBase[Dignity, DignityCreate, DignityUpdate, DignityFilter]):
    pass


dignity = CRUDDignity(Dignity)
