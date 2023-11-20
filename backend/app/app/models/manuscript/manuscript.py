from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, SmallInteger, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.base_class import Base, intpk, unique_slug
from .fund import Fund
from .page import Page
from ..year import Year

if TYPE_CHECKING:
    from .bookmark import Bookmark


class Manuscript(Base):
    id: Mapped[intpk]

    title: Mapped[str | None] = mapped_column(String(170), index=True)
    neb_slug: Mapped[unique_slug | None]
    code_title: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    code: Mapped[str] = mapped_column(String(36), unique=True, index=True)
    handwriting: Mapped[int] = mapped_column(SmallInteger, index=True)
    num_bookmarks: Mapped[enums.NumBookmarks | None] = mapped_column(index=True)
    not_numbered_pages: Mapped[list[dict[str, int]]] = mapped_column(JSON)
    first_page_position: Mapped[enums.PagePosition]
    all_num_pages: Mapped[int | None] = mapped_column(SmallInteger)

    year_id: Mapped[int] = mapped_column(ForeignKey(Year.id), index=True)
    fund_id: Mapped[int | None] = mapped_column(ForeignKey(Fund.id), index=True)
    # preview_page_id: Mapped[int | None] = mapped_column(ForeignKey(Page.id, ondelete="CASCADE"))
    preview_page_id: Mapped[int | None] = mapped_column(ForeignKey(Page.id))

    year: Mapped[Year] = relationship(back_populates='manuscripts')
    fund: Mapped[Fund | None] = relationship(back_populates='manuscripts')
    preview_page: Mapped[Page | None] = relationship(foreign_keys=[preview_page_id])

    bookmarks: Mapped[list[Bookmark]] = relationship(back_populates='manuscript')
