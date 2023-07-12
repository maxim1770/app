from pydantic import BaseModel

from app.models import HolidayCategory
from app.schemas import HolidayCategoryCreate, HolidayCategoryUpdate
from ..base import CRUDBase


class HolidayCategoryFilter(BaseModel):
    pass


class CRUDHolidayCategory(
    CRUDBase[HolidayCategory, HolidayCategoryCreate, HolidayCategoryUpdate, HolidayCategoryFilter]
):
    pass


holiday_category = CRUDHolidayCategory(HolidayCategory)
