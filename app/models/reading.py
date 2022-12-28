from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Reading(Base):
    __tablename__ = "readings"
    id = Column(Integer, primary_key=True)

    movable_date_id = Column(Integer, ForeignKey("movable_dates.id"))
    movable_date = relationship("MovableDate", back_populates="readings")

    zachalo_id = Column(Integer, ForeignKey("zachalos.id"))
    zachalo = relationship("Zachalo", back_populates="readings")

    test_field = Column(Integer)
    test_field_2 = Column(Integer)
