from sqlalchemy.orm import Session

from app.db import base  # noqa: F401
from app.db.base_class import Base
from app.db.session import engine


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
