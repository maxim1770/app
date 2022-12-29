from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship, backref

from app.db.session import Base


class SaintLive(Base):
    __tablename__ = "saints_lives"

    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    # book = relationship("Book", backref=backref("saint_live", uselist=False))
    book = relationship("Book", back_populates="saint_live")

    test_field = Column(String)

    # saint_id = Column(Integer, ForeignKey("saints.id"))
    # saint = relationship("Saint", back_populates="saints_lives")
