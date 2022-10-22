from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Week(Base):
    __tablename__ = "weeks"
    id = Column(Integer, primary_key=True)

    title = Column(String)
    num = Column(Integer)
    sunday_title = Column(String)
    sunday_num = Column(Integer)

    days = relationship("Day", back_populates="week")

    period_id = Column(Integer, ForeignKey("periods.id"))
    period = relationship("Period", back_populates="weeks")
