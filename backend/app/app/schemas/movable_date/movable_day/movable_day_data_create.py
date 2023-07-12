from pydantic import BaseModel, conint

from app import enums


class MovableDayGet(BaseModel):
    cycle_num: enums.CycleNum
    sunday_num: conint(strict=True, ge=1, le=36) | None
    abbr: enums.MovableDayAbbr
