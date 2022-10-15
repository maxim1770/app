from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)

    date = relationship("Date", back_populates="owner")
    book = relationship("Book", back_populates="owner")


class Date(Base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(String, index=True)
    week = Column(Integer, index=True)
    period = Column(Integer, index=True)

    owner_id = Column(Integer, ForeignKey("readings.id"))

    owner = relationship("Reading", back_populates="dates")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, index=True)
    zachalo = Column(Integer, index=True)

    owner_id = Column(Integer, ForeignKey("readings.id"))

    owner = relationship("Reading", back_populates="books")
