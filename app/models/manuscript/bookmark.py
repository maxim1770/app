from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base, intpk
from .manuscript import Manuscript
from .page import Page
from ..book import Book


class Bookmark(Base):
    manuscript_id: Mapped[intpk] = mapped_column(ForeignKey(Manuscript.id))
    book_id: Mapped[intpk] = mapped_column(ForeignKey(Book.id))

    manuscript: Mapped[Manuscript] = relationship(back_populates='books')
    book: Mapped[Book] = relationship(back_populates='manuscripts')

    first_page_id: Mapped[int] = mapped_column(ForeignKey(Page.id))
    end_page_id: Mapped[int] = mapped_column(ForeignKey(Page.id))

    first_page: Mapped[Page] = relationship(foreign_keys=[first_page_id])
    end_page: Mapped[Page] = relationship(foreign_keys=[end_page_id])
