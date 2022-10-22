from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Zachalo(Base):
    __tablename__ = "zachalos"
    id = Column(Integer, primary_key=True)

    num = Column(Integer)

    readings = relationship("Reading", back_populates="zachalo")

    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="zachalos")
