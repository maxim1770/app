from sqlalchemy import Integer, Column
from sqlalchemy.orm import relationship

from app.db.session import Base


class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True)

    month = Column(Integer)
    day = Column(Integer)

    holidays = relationship("Holiday", back_populates="day")
