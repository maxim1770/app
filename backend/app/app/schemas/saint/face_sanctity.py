from pydantic import BaseModel

from app import enums


class FaceSanctityBase(BaseModel):
    title: enums.FaceSanctityTitle


class FaceSanctityCreate(FaceSanctityBase):
    pass


class FaceSanctity(FaceSanctityBase):
    id: int

    # saints: list[Saint] = []

    class Config:
        orm_mode = True
