from typing import Any

from dotenv import load_dotenv
from pydantic import field_validator, PostgresDsn, FieldValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'

    BACKEND_CORS_ORIGINS: list[str] = [
        'http://localhost',
        'http://localhost:5173',
        'http://localhost:5174',
        'http://localhost:5175',
        'http://localhost:5176',
        'http://localhost:8000', 'http://localhost:8080', 'http://localhost:8081', 'http://localhost:81'
    ]

    @field_validator('BACKEND_CORS_ORIGINS', mode='before')
    @classmethod
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int
    SQLALCHEMY_DATABASE_URI: URL | None = None

    @field_validator('SQLALCHEMY_DATABASE_URI', mode='before')
    @classmethod
    def assemble_db_connection(cls, v: str | None, info: FieldValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        SQLALCHEMY_DATABASE_URI: URL = URL.create(
            'postgresql',
            username=info.data['POSTGRES_USER'],
            password=info.data['POSTGRES_PASSWORD'],
            host=info.data['POSTGRES_SERVER'],
            port=info.data['POSTGRES_PORT'],
            database=info.data['POSTGRES_DB']
        )
        return SQLALCHEMY_DATABASE_URI

    DATA_CREATE_DIR: str = './backend/app/app/create/data'
    TEST_DATA_DIR: str = './backend/app/app/tests/data'
    DATA_DIR: str = '../../../data'
    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
