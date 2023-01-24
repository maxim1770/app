from typing import Any

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = ['http://localhost', 'http://localhost:8080']

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme='postgresql',
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('POSTGRES_SERVER'),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    DATA_CREATE_DIR: str = './app/create/data'

    class Config:
        case_sensitive = True


settings = Settings()
