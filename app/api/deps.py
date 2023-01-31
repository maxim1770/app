from typing import Generator

import requests

from app.db.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_session() -> Generator:
    session = requests.Session()
    try:
        yield session
    finally:
        session.close()
