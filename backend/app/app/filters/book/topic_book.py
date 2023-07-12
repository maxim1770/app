import logging

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import field_validator

from app import models


class TopicBookFilter(Filter):
    id__isnull: bool | None
    topics__like: str | list[str] | None

    @field_validator("topics__like")
    @classmethod
    def topics__like_(cls, value):
        if value is None:
            return None
        logging.info([value])
        if isinstance(value, str):
            return [value]
        return value

    class Constants(Filter.Constants):
        model = models.TopicBook
