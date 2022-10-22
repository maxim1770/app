from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Period(Base):
    __tablename__ = "periods"
    id = Column(Integer, primary_key=True)

    title = Column(String)
    num = Column(Integer)

    weeks = relationship("Week", back_populates="period")