from sqlalchemy import SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk


class Page(Base):
    id: Mapped[intpk]

    num: Mapped[int] = mapped_column(SmallInteger, index=True)
    position: Mapped[enums.PagePosition]
