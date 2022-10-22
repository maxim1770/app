from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base

class Date(Base):
    __tablename__ = "dates"
    id = Column(Integer, primary_key=True)

    divine_service = Column(String)

    readings = relationship("Reading", back_populates="date")

    day_id = Column(Integer, ForeignKey("days.id"))
    day = relationship("Day", back_populates="dates")