from enum import StrEnum, auto


class ObjectStorageClass(StrEnum):
    STANDARD = auto()
    STANDARD_IA = auto()  # Холодное
    GLACIER = auto()
