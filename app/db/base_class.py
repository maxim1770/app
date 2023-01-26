import re
from typing import Pattern

from sqlalchemy import MetaData, String
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import mapped_column
from typing_extensions import Annotated

REGEX_CAMEL_TO_SNAKE: Pattern[str] = re.compile(r'(?<!^)(?=[A-Z])')

intpk = Annotated[int, mapped_column(primary_key=True)]
unique_slug = Annotated[str, mapped_column(String(150), unique=True)]

metadata_obj = MetaData()


class Base(DeclarativeBase):
    metadata = metadata_obj

    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:
        return REGEX_CAMEL_TO_SNAKE.sub('_', cls.__name__).lower()
