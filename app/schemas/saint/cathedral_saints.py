from enum import Enum

from pydantic import BaseModel

from app.schemas.saint.saint import Saint


class CathedralSaintsTitle(str, Enum):
    pass


class CathedralSaintsBase(BaseModel):
    title: CathedralSaintsTitle


class CathedralSaintsCreate(CathedralSaintsBase):
    pass


class CathedralSaints(CathedralSaintsBase):
    id: int

    date_id: int

    saints: list[Saint] = []

    class Config:
        orm_mode = True
