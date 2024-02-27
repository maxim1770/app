from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from .day import Day
from .movable_date import MovableDay
from .post import Post


class Date(Base):
    day_id: Mapped[int] = mapped_column(ForeignKey(Day.id), primary_key=True, index=True)
    movable_day_id: Mapped[int] = mapped_column(ForeignKey(MovableDay.id), primary_key=True)

    year: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    is_solid_week: Mapped[bool | None]

    post_id: Mapped[int | None] = mapped_column(ForeignKey(Post.id), index=True)
    post: Mapped[Post | None] = relationship(back_populates='dates')

    day: Mapped[Day] = relationship(back_populates='movable_days')
    movable_day: Mapped[MovableDay] = relationship(back_populates='days')
