from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class BibleBook(Base):
    __tablename__ = "bible_books"
    id = Column(Integer, primary_key=True)

    testament = Column(String)
    testament_ru = Column(String)

    part = Column(String)
    part_ru = Column(String)

    title = Column(String)
    abbr = Column(String)
    abbr_ru = Column(String)

    zachalos = relationship("Zachalo", back_populates="bible_book")
