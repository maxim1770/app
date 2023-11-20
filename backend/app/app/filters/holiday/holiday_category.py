from fastapi_filter.contrib.sqlalchemy import Filter

from app import models, enums


class HolidayCategoryFilter(Filter):
    title: enums.HolidayCategoryTitle | None = None

    class Constants(Filter.Constants):
        model = models.HolidayCategory
