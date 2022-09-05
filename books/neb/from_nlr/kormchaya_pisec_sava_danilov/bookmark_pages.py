"""
Страница закладок для рукописи [neb](https://kp.rusneb.ru/item/material/kormchaya-pisec-sava-danilov)

"""
from pathlib import Path

from crs.schemes import BookmarkPagesTurnoverModel, PageTurnover, TurnoverEnum

bookmark_pages_turnover: BookmarkPagesTurnoverModel = BookmarkPagesTurnoverModel(
    first_week_number=1
    ,
    pages_list=(PageTurnover(page=41
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Правила святых Апостолов'
                             ,
                             number_rules=85
                             ),
                PageTurnover(page=56
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Святого Апостола Павла особно правил'
                             ,
                             number_rules=17
                             ),
                PageTurnover(page=57
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Того ж правила о усопших и властелех'
                             ,
                             number_rules=2
                             ),
                PageTurnover(page=58
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Первый Вселенский Собор - Никейский'
                             ,
                             number_rules=20
                             ),
                PageTurnover(page=65
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Поместный Собор - Анкирский'
                             ,
                             number_rules=25
                             ),
                PageTurnover(page=72
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Поместный Собор - Неокесарийский'
                             ,
                             number_rules=14
                             ),
                PageTurnover(page=74
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Гангрский'
                             ,
                             number_rules=19
                             ),
                PageTurnover(page=77
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Антиохийский'
                             ,
                             number_rules=25
                             ),
                PageTurnover(page=84
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Лаодикийский'
                             ,
                             number_rules=58
                             ),
                PageTurnover(page=94
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Второй Вселенский Собор - Константинопольский'
                             ,
                             number_rules=8
                             ),
                PageTurnover(page=97
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Третий Вселенский Собор - Эфесский'
                             ,
                             # Послание записано как девятое правило и как отдельная глава вi(12)
                             number_rules=8
                             ),
                PageTurnover(page=99
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             # Название с головы и немного с рукописи 304-i/f-304i-206
                             title='Третий Вселенский Собор - Эфесский: послание к священному собору Памфилийскому'
                             ,
                             number_rules=1
                             ),
                ),
    const_week_page=(1, 41)
    ,
    pdf_plus_pages=7
    ,
    pdf_path=Path(r"C:\Users\MaxDroN\pravoslavie\canons\kormchij\kormchaya_pisec_sava_danilov.pdf")
)
