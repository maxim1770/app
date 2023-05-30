import logging

from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import validator

from app import models


class TopicBookFilter(Filter):
    id__isnull: bool | None
    topics__like: str | list[str] | None

    @validator("topics__like")
    def topics__like_(cls, value):
        if value is None:
            return None
        logging.info([value])
        if isinstance(value, str):
            return [value]
        return value

    class Constants(Filter.Constants):
        model = models.TopicBook
