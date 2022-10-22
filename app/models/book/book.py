from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)

    new_or_old_testament = Column(String)
    section = Column(String)
    title = Column(String)
    title_short_en = Column(String)

    zachalos = relationship("Zachalo", back_populates="book")
