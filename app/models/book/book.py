from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)

    title = Column(String)

    saint_live = relationship("SaintLive", back_populates="book", uselist=False)
