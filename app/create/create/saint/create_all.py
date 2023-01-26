import logging

from sqlalchemy.orm import Session

from app.api import deps
from .dignity import create_dignities
from .face_sanctity import create_faces_sanctity

if __name__ == '__main__':
    db: Session = deps.get_db().__next__()

    # create_dignities(db)
    # create_faces_sanctity(db)
