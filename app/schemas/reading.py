from pydantic import BaseModel


class ReadingBase(BaseModel):
    pass


class ReadingCreate(ReadingBase):
    pass


class Reading(ReadingBase):
    id: int

    movable_date_id: int
    zachalo_id: int

    class Config:
        orm_mode = True
