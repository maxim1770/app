from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class MovableDate(Base):
    __tablename__ = "movable_dates"
    id = Column(Integer, primary_key=True)

    movable_day_id = Column(Integer, ForeignKey("movable_days.id"))
    movable_day = relationship("MovableDay", back_populates="movable_dates")

    divine_service_id = Column(Integer, ForeignKey("divine_services.id"))
    divine_service = relationship("DivineService", back_populates="movable_dates")

    readings = relationship("Reading", back_populates="movable_date")
