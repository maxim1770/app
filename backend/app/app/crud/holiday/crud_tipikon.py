import sqlalchemy as sa
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import enums
from app.models import Tipikon
from app.schemas import TipikonCreate, TipikonUpdate
from ..base import CRUDBase


class TipikonFilter(BaseModel):
    pass


class CRUDTipikon(CRUDBase[Tipikon, TipikonCreate, TipikonUpdate, TipikonFilter]):
    pass


tipikon = CRUDTipikon(Tipikon)
