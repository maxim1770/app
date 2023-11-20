from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from .manuscript import Manuscript
from .page import Page
from ..book import Book


class Bookmark(Base):
    manuscript_id: Mapped[int] = mapped_column(ForeignKey(Manuscript.id), primary_key=True, index=True)
    book_id: Mapped[int] = mapped_column(ForeignKey(Book.id), primary_key=True, index=True)

    manuscript: Mapped[Manuscript] = relationship(back_populates='bookmarks')
    book: Mapped[Book] = relationship(back_populates='bookmarks')

    first_page_id: Mapped[int] = mapped_column(
        ForeignKey(Page.id),
        index=True
    )
    end_page_id: Mapped[int] = mapped_column(
        ForeignKey(Page.id),
        index=True
    )

    first_page: Mapped[Page] = relationship(
        foreign_keys=[first_page_id],
        cascade='all, delete-orphan',
        single_parent=True
    )
    end_page: Mapped[Page] = relationship(
        foreign_keys=[end_page_id],
        cascade='all, delete-orphan',
        single_parent=True
    )

    chapter_num: Mapped[int | None] = mapped_column(SmallInteger, index=True)
