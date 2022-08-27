import json

from pydantic import BaseModel
from pydantic import parse_obj_as


class PagesModel(BaseModel):
    week_number: int
    first_page: int
    last_page: int


class ListPagesModel(BaseModel):
    __root__: list[PagesModel]


l = ListPagesModel(__root__=[])


class DataPagesModel(BaseModel):
    first_week_number: int
    pages_list: list[int]

    const_week_page: tuple[int, int]


data_model = DataPagesModel(
    first_week_number=1,
    pages_list=(180, 187, 192, 199, 207, 215, 223, 231, 236, 244, 252, 259, 265, 269,
                275, 281, 287, 294, 300,
                308, 313, 322, 332, 339,
                345, 354, 362, 369, 376,
                383, 391, 397, 405
                ),
    const_week_page=(1, 180)
)

if data_model.const_week_page != (data_model.first_week_number, data_model.pages_list[0]):
    raise ValueError("Проверь соотношение страниц и номеров недель!")

for i in range(len(data_model.pages_list) - 1):
    l.__root__.append(PagesModel(week_number=data_model.first_week_number + i
                                 ,
                                 first_page=data_model.pages_list[i]
                                 ,
                                 last_page=data_model.pages_list[i + 1]
                                 ),
                      )

with open('data_3.json', 'w', encoding='utf-8') as f:
    json.dump(l.dict(), f, indent=4, ensure_ascii=False)
