from pydantic import BaseModel

from app.models import FaceSanctity
from app.schemas import FaceSanctityCreate, FaceSanctityUpdate
from ..base import CRUDBase


class FaceSanctityFilter(BaseModel):
    pass


class CRUDFaceSanctity(CRUDBase[FaceSanctity, FaceSanctityCreate, FaceSanctityUpdate, FaceSanctityFilter]):
    pass


face_sanctity = CRUDFaceSanctity(FaceSanctity)
