import sqlalchemy as sa
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.session import Base


class SaintLive(Base):
    __tablename__ = 'saints_lives'

    book_id = mapped_column(sa.ForeignKey('books.id'), primary_key=True)

    # book = relationship('Book', backref=backref('saint_live', uselist=False))
    book: Mapped['Book'] = relationship(back_populates='saint_live')

    # saint_id = Column(Integer, ForeignKey('saints.id'))
    # saint = relationship('Saint', back_populates='saints_lives')
