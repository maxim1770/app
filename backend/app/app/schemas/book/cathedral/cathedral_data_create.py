from pydantic import BaseModel

from app.schemas.year import YearCreate
from .cathedral import CathedralCreate


class CathedralDataCreate(BaseModel):
    cathedral_in: CathedralCreate
    year_in: YearCreate | None = None
