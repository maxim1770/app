from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True)

    date_id = Column(Integer, ForeignKey("dates.id"))
    date = relationship("Date", back_populates="readings")

    bible_zachalo_id = Column(Integer, ForeignKey("bible_zachalos.id"))
    bible_zachalo = relationship("BibleZachalo", back_populates="readings")


class Date(Base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True)

    day = Column(String)
    week = Column(Integer)
    period = Column(Integer)

    readings = relationship("Reading", back_populates="date")


class BibleZachalo(Base):
    __tablename__ = "bible_zachalos"

    id = Column(Integer, primary_key=True)

    zachalo = Column(Integer)

    readings = relationship("Reading", back_populates="bible_zachalo")

    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="bible_zachalos")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)

    new_or_old_testament = Column(String)
    section = Column(String)
    title = Column(String)
    title_short_en = Column(String)

    bible_zachalos = relationship("BibleZachalo", back_populates="book")
