from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Saint(Base):
    __tablename__ = "saints"
    id = Column(Integer, primary_key=True)

    name = Column(String)
    name_en = Column(String)

    dignity_id = Column(Integer, ForeignKey("dignities.id"))
    dignity = relationship("Dignity", back_populates="saints")

    face_sanctity_id = Column(Integer, ForeignKey("faces_sanctity.id"))
    face_sanctity = relationship("FaceSanctity", back_populates="saints")

    holidays = relationship("Holiday", back_populates="saint")

    # saints_lives = relationship("SaintLive", back_populates="saint")
