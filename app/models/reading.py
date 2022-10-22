from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Reading(Base):
    __tablename__ = "readings"
    id = Column(Integer, primary_key=True)

    date_id = Column(Integer, ForeignKey("dates.id"))
    date = relationship("Date", back_populates="readings")

    zachalo_id = Column(Integer, ForeignKey("zachalos.id"))
    zachalo = relationship("Zachalo", back_populates="readings")
