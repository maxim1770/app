import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base


class Saint(Base):
    __tablename__ = 'saints'
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str | None] = mapped_column(sa.String(100), unique=True)
    name_en: Mapped[str] = mapped_column(sa.String(50), unique=True)

    dignity_id = mapped_column(sa.ForeignKey('dignities.id'))
    face_sanctity_id = mapped_column(sa.ForeignKey('faces_sanctity.id'))

    dignity: Mapped['Dignity'] = relationship(back_populates='saints')
    face_sanctity: Mapped['FaceSanctity'] = relationship(back_populates='saints')

    holidays: Mapped[list['Holiday']] = relationship(back_populates='saint')

    # saints_lives = relationship('SaintLive', back_populates='saint')
