from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class CathedralSaints(Base):
    __tablename__ = "cathedrals_saints"
    id = Column(Integer, primary_key=True)

    title = Column(String)

    # date_id = Column(Integer, ForeignKey("dates.id"))
    # date = relationship("Date", back_populates="cathedrals_saints")
