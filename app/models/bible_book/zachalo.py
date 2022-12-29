from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Zachalo(Base):
    __tablename__ = "zachalos"
    id = Column(Integer, primary_key=True)

    num = Column(Integer)
    title = Column(String)

    readings = relationship("Reading", back_populates="zachalo")

    bible_book_id = Column(Integer, ForeignKey("bible_books.id"))
    bible_book = relationship("BibleBook", back_populates="zachalos")
