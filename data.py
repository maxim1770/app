import json

from pydantic import BaseModel
from pydantic import parse_obj_as


class PagesModel(BaseModel):
    week_number: int
    first_page: int
    last_page: int


class ListPagesModel(BaseModel):
    __root__: list[PagesModel]


l = ListPagesModel.parse_obj([
    PagesModel(week_number=10
               ,
               first_page=244
               ,
               last_page=252
               ),
    PagesModel(week_number=11
               ,
               first_page=252
               ,
               last_page=259
               ),
    PagesModel(week_number=12
               ,
               first_page=259
               ,
               last_page=265
               ),
    PagesModel(week_number=13
               ,
               first_page=265
               ,
               last_page=269
               ),
    PagesModel(week_number=14
               ,
               first_page=269
               ,
               last_page=275
               ),
    PagesModel(week_number=15
               ,
               first_page=275
               ,
               last_page=281
               ),
    PagesModel(week_number=16
               ,
               first_page=281
               ,
               last_page=287
               ),
    PagesModel(week_number=17
               ,
               first_page=287
               ,
               last_page=294
               ),
    PagesModel(week_number=18
               ,
               first_page=294
               ,
               last_page=300
               ),
    PagesModel(week_number=19
               ,
               first_page=300
               ,
               last_page=308
               ),

])


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(l.dict(), f, indent=4, ensure_ascii=False)
