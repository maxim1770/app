from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Year(Base):
    __tablename__ = "years"
    id = Column(Integer, primary_key=True)

    title = Column(String)
    _year = Column(Integer)  # TODO: тут потом заменить на тип данных YEAR или Date

    holidays = relationship("Holiday", back_populates="year")
