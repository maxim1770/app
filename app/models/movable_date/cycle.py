from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Cycle(Base):
    __tablename__ = "cycles"
    id = Column(Integer, primary_key=True)

    num = Column(Integer)
    title = Column(String)


    weeks = relationship("Week", back_populates="cycle")
