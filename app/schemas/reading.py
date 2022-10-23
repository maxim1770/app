from pydantic import BaseModel


class ReadingBase(BaseModel):
    pass


class ReadingCreate(ReadingBase):
    pass


class Reading(ReadingBase):
    id: int
    divine_service_id: int
    num_id: int

    class Config:
        orm_mode = True
