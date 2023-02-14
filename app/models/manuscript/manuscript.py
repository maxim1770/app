from uuid import UUID

from sqlalchemy import ForeignKey, String, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.types import Uuid

from app.db.base_class import Base, intpk, unique_slug
from .fund import Fund
from ..year import Year


class Manuscript(Base):
    id: Mapped[intpk]

    title: Mapped[str | None] = mapped_column(String(170))
    neb_slug: Mapped[unique_slug | None]
    code_title: Mapped[str] = mapped_column(String(15), unique=True)
    code: Mapped[UUID | str] = mapped_column(Uuid, unique=True)
    handwriting: Mapped[int] = mapped_column(SmallInteger)

    year_id: Mapped[int] = mapped_column(ForeignKey(Year.id))
    fund_id: Mapped[int] = mapped_column(ForeignKey(Fund.id))

    year: Mapped[Year] = relationship(back_populates='manuscripts')
    fund: Mapped[Fund] = relationship(back_populates='manuscripts')
