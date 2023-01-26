from app.models.saint import Saint
from app.schemas.saint import SaintCreate, SaintUpdate
from ..base import CRUDBase

saint = CRUDBase[Saint, SaintCreate, SaintUpdate](Saint)
