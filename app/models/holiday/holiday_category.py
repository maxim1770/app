from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class HolidayCategory(Base):
    __tablename__ = "holidays_categories"
    id = Column(Integer, primary_key=True)

    title = Column(String)

    holidays = relationship("Holiday", back_populates="holiday_category")
