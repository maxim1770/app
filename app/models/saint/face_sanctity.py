from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.session import Base


class FaceSanctity(Base):
    __tablename__ = 'faces_sanctity'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[enums.FaceSanctityTitle] = mapped_column(unique=True)

    saints: Mapped[list['Saint']] = relationship(back_populates='face_sanctity')
