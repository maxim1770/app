from pydantic import BaseModel
from app.schemas.saint.saint import Saint


class SaintLiveBase(BaseModel):
    test_field: str


class SaintLiveCreate(SaintLiveBase):
    pass


class SaintLive(SaintLiveBase):
    # book_id: int

    # saint: Saint | None = None

    class Config:
        orm_mode = True
