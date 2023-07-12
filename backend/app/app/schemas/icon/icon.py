from pydantic import constr

from ..base import SchemaBase


class __IconBase(SchemaBase):
    desc: constr(strip_whitespace=True, strict=True, max_length=450) | None = None
    pravicon_id: int | None = None
    gallerix_id: int | None = None
    shm_id: int | None = None


class IconCreate(__IconBase):
    pass


class IconUpdate(__IconBase):
    pass
