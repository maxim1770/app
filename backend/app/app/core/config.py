from dotenv import load_dotenv
from pydantic import field_validator, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    PROJECT_NAME: str

    BACKEND_CORS_ORIGINS: list[str]

    @field_validator('BACKEND_CORS_ORIGINS', mode='before')
    @classmethod
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    OBJECT_STORAGE_BUCKET_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> URL:
        return URL.create(
            'postgresql',
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            database=self.POSTGRES_DB
        )

    TG_BOT_TOKEN: str
    TG_CHANNEL_ID: str

    VK_GROUP_ID: str
    VK_ACCESS_TOKEN: str

    DATA_CREATE_DIR: str = './backend/app/app/create/data'
    TEST_DATA_DIR: str = './backend/app/app/tests/data'
    DATA_DIR: str = '../../../data'

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
