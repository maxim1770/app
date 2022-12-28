from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class FaceSanctity(Base):
    __tablename__ = "faces_sanctity"
    id = Column(Integer, primary_key=True)

    title = Column(String)

    saints = relationship("Saint", back_populates="face_sanctity")
