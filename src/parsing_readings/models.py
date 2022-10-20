from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Reading(Base):
    __tablename__ = "readings"
    id = Column(Integer, primary_key=True)

    date_id = Column(Integer, ForeignKey("dates.id"))
    date = relationship("Date", back_populates="readings")

    zachalo_id = Column(Integer, ForeignKey("zachalos.id"))
    zachalo = relationship("Zachalo", back_populates="readings")


class Zachalo(Base):
    __tablename__ = "zachalos"
    id = Column(Integer, primary_key=True)

    num = Column(Integer)

    readings = relationship("Reading", back_populates="zachalo")

    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="zachalos")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)

    new_or_old_testament = Column(String)
    section = Column(String)
    title = Column(String)
    title_short_en = Column(String)

    zachalos = relationship("Zachalo", back_populates="book")


class Date(Base):
    __tablename__ = "dates"
    id = Column(Integer, primary_key=True)

    day = Column(String)
    day_title = Column(String)
    divine_service = Column(String)

    readings = relationship("Reading", back_populates="date")

    week_id = Column(Integer, ForeignKey("weeks.id"))
    week = relationship("Week", back_populates="dates")


class Week(Base):
    __tablename__ = "weeks"
    id = Column(Integer, primary_key=True)

    title = Column(String)
    num = Column(Integer)
    sunday_title = Column(String)
    sunday_num = Column(Integer)

    dates = relationship("Date", back_populates="week")

    period_id = Column(Integer, ForeignKey("periods.id"))
    period = relationship("Period", back_populates="weeks")


class Period(Base):
    __tablename__ = "periods"
    id = Column(Integer, primary_key=True)

    title = Column(String)
    num = Column(Integer)

    weeks = relationship("Week", back_populates="period")
