from app.filters import TipikonFilter
from app.models import Tipikon
from app.schemas import TipikonCreate, TipikonUpdate

from ..base import CRUDBase


class CRUDTipikon(CRUDBase[Tipikon, TipikonCreate, TipikonUpdate, TipikonFilter]):
    pass


tipikon = CRUDTipikon(Tipikon)
