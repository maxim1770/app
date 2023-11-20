from app.filters import FaceSanctityFilter

from app.models import FaceSanctity
from app.schemas import FaceSanctityCreate, FaceSanctityUpdate
from ..base import CRUDBase


class CRUDFaceSanctity(CRUDBase[FaceSanctity, FaceSanctityCreate, FaceSanctityUpdate, FaceSanctityFilter]):
    pass


face_sanctity = CRUDFaceSanctity(FaceSanctity)
