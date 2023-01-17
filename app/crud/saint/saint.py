from app.crud.base import CRUDBase
from app.models.saint import Saint
from app.schemas.saint import SaintCreate, SaintUpdate

saint = CRUDBase[Saint, SaintCreate, SaintUpdate](Saint)
