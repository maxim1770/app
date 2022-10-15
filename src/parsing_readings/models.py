from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)

    date_id = Column(Integer, ForeignKey("dates.id"))
    date = relationship("Date", back_populates="readings")

    bible_zachalo_id = Column(Integer, ForeignKey("bible_zachalos.id"))
    bible_zachalo = relationship("BibleZachalo", back_populates="readings")


class Date(Base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(String, index=True)
    week = Column(Integer, index=True)
    period = Column(Integer, index=True)

    readings = relationship("Reading", back_populates="date")


class BibleZachalo(Base):
    __tablename__ = "bible_zachalos"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, index=True)
    zachalo = Column(Integer, index=True)

    readings = relationship("Reading", back_populates="bible_zachalo")
