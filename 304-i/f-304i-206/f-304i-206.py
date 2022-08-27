import json

from pydantic import BaseModel
from pydantic import parse_obj_as
from pathlib import Path


class PagesModel(BaseModel):
    week_number: int
    first_page: int
    last_page: int


class ListPagesModel(BaseModel):
    __root__: list[PagesModel]


pages_models = ListPagesModel(__root__=[])


class DataPagesModel(BaseModel):
    first_week_number: int
    pages_list: list[int]

    const_week_page: tuple[int, int]


data_model = DataPagesModel(
    first_week_number=1,
    pages_list=(27, 42, 43, 44, 51, 59, 62, 65, 72, 81, 84
                ),
    const_week_page=(1, 24)
)

if data_model.const_week_page != (data_model.first_week_number, data_model.pages_list[0]):
    raise ValueError("Проверь соотношение страниц и номеров недель!")

for i in range(len(data_model.pages_list) - 1):
    pages_models.__root__.append(PagesModel(week_number=data_model.first_week_number + i
                                            ,
                                            first_page=data_model.pages_list[i]
                                            ,
                                            last_page=data_model.pages_list[i + 1]
                                            ),
                                 )

# Получить имя скрипта (без .py), из которого выполняется этот кот
# Код ниже выдаст строку str: f-304i-206
# {Path(__file__).stem}
with open(f'data/pages.json', 'w', encoding='utf-8') as f:
    json.dump(pages_models.dict(), f, indent=4, ensure_ascii=False)
