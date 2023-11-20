from app.filters import HolidayCategoryFilter
from app.models import HolidayCategory
from app.schemas import HolidayCategoryCreate, HolidayCategoryUpdate

from ..base import CRUDBase


class CRUDHolidayCategory(
    CRUDBase[HolidayCategory, HolidayCategoryCreate, HolidayCategoryUpdate, HolidayCategoryFilter]
):
    pass


holiday_category = CRUDHolidayCategory(HolidayCategory)
