from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Holiday(Base):
    __tablename__ = "holidays"
    id = Column(Integer, primary_key=True)

    title = Column(String)
    title_en = Column(String)

    holiday_category_id = Column(Integer, ForeignKey("holidays_categories.id"))
    holiday_category = relationship("HolidayCategory", back_populates="holidays")

    year_id = Column(Integer, ForeignKey("years.id"))
    year = relationship("Year", back_populates="holidays")

    day_id = Column(Integer, ForeignKey("days.id"))
    day = relationship("Day", back_populates="holidays")

    saint_id = Column(Integer, ForeignKey("saints.id"))
    saint = relationship("Saint", back_populates="holidays")
