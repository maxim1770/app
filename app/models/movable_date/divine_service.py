from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base

class DivineService(Base):
    __tablename__ = "divine_services"
    id = Column(Integer, primary_key=True)

    title = Column(String)

    readings = relationship("Reading", back_populates="divine_service")

    day_id = Column(Integer, ForeignKey("days.id"))
    day = relationship("Day", back_populates="divine_services")