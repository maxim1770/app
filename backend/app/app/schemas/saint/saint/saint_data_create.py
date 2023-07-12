from pydantic import BaseModel

from app import enums
from .saint import SaintUpdate, SaintCreate


class __SaintDataBase(BaseModel):
    saint_in: SaintUpdate | None = None
    face_sanctity_title: enums.FaceSanctityTitle | None = None
    dignity_title: enums.DignityTitle | None = None


class SaintDataCreate(__SaintDataBase):
    saint_in: SaintCreate


class SaintDataUpdate(__SaintDataBase):
    pass
