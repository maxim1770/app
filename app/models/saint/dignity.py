from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.session import Base


class Dignity(Base):
    __tablename__ = 'dignities'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[enums.DignityTitle] = mapped_column(unique=True)

    saints: Mapped[list['Saint']] = relationship(back_populates='dignity')
