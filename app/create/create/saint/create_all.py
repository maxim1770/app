import logging

from sqlalchemy.orm import Session

from app.api import deps
from app.create.create.saint.dignity import create_dignities
from app.create.create.saint.face_sanctity import create_faces_sanctity
from app.db.session import engine, Base

if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    Base.metadata.create_all(bind=engine)

    # create_dignities(db)
    # create_faces_sanctity(db)
