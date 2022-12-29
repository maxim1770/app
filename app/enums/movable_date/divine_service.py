from enum import auto

from fastapi_utils.enums import StrEnum


class DivineServiceTitle(StrEnum):
    liturgy = auto()
    matins = auto()
    vespers = auto()
