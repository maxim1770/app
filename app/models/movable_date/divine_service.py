from sqlalchemy.orm import relationship, Mapped, mapped_column

from app import enums
from app.db.session import Base


class DivineService(Base):
    __tablename__ = 'divine_services'
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[enums.DivineServiceTitle] = mapped_column(unique=True)

    movable_dates: Mapped[list['MovableDate']] = relationship(back_populates='divine_service')
