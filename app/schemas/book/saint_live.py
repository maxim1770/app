from pydantic import BaseModel


class SaintLiveBase(BaseModel):
    test_field: str


class SaintLiveCreate(SaintLiveBase):
    pass


class SaintLive(SaintLiveBase):
    book_id: int

    # saint: Saint | None = None

    class Config:
        orm_mode = True
