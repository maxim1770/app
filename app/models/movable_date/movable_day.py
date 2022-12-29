from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class MovableDay(Base):
    __tablename__ = "movable_days"
    id = Column(Integer, primary_key=True)

    abbr = Column(String)
    abbr_ru = Column(String)
    title = Column(String)

    week_id = Column(Integer, ForeignKey("weeks.id"))
    week = relationship("Week", back_populates="days")

    movable_dates = relationship("MovableDate", back_populates="movable_day")
