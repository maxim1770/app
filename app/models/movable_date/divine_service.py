from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class DivineService(Base):
    __tablename__ = "divine_services"
    id = Column(Integer, primary_key=True)

    title = Column(String)

    movable_dates = relationship("MovableDate", back_populates="divine_service")
