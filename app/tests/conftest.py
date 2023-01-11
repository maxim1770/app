from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import Session

from app.tests.test_utils import *
from app.api.deps import get_db
from app.db.session import Base
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

    app.dependency_overrides[get_db] = get_db_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
