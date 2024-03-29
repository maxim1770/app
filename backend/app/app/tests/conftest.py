from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import Session

from app.api import deps
from app.db.base_class import Base
from app.main import app


@pytest.fixture(name="db")
def db_fixture() -> Generator:
    engine = create_engine(
        'sqlite://',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)

    with Session(engine) as db:
        yield db


@pytest.fixture(name="client")
def client_fixture(db: Session) -> Generator:
    def get_db_override():
        return db

    app.dependency_overrides[deps.get_db] = get_db_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture(name="session", scope='session')
def session_fixture() -> Generator:
    yield next(deps.get_session())
