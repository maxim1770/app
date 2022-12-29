from pydantic import BaseModel

from app import enums
from app.schemas.saint.saint import Saint


class FaceSanctityBase(BaseModel):
    title: enums.FaceSanctityTitle


class FaceSanctityCreate(FaceSanctityBase):
    pass


class FaceSanctity(FaceSanctityBase):
    id: int

    saints: list[Saint] = []

    class Config:
        orm_mode = True
