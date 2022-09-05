"""
Страница закладок для рукописи [neb](https://kp.rusneb.ru/item/material/kormchaya-4)

"""
from pathlib import Path

from crs.schemes import BookmarkPagesTurnoverModel, PageTurnover, TurnoverEnum

bookmark_pages_turnover: BookmarkPagesTurnoverModel = BookmarkPagesTurnoverModel(
    first_week_number=1
    ,
    pages_list=(PageTurnover(page=35
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Правила святых Апостолов'
                             ,
                             number_rules=85
                             ),
                PageTurnover(page=51
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Святого Апостола Павла особно правил'
                             ,
                             number_rules=17
                             ),
                PageTurnover(page=52
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Того ж правила о усопших и властелех'
                             ,
                             number_rules=2
                             ),
                PageTurnover(page=53
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Первый Вселенский Собор - Никейский'
                             ,
                             number_rules=20
                             ),
                PageTurnover(page=60
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Анкирский'
                             ,
                             number_rules=25
                             ),
                PageTurnover(page=67
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Неокесарийский'
                             ,
                             number_rules=14
                             ),
                PageTurnover(page=69
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Гангрский'
                             ,
                             number_rules=19
                             ),
                PageTurnover(page=72
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Антиохийский'
                             ,
                             number_rules=25
                             ),
                PageTurnover(page=79
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Поместный Собор - Лаодикийский'
                             ,
                             number_rules=58
                             ),
                PageTurnover(page=88
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Второй Вселенский Собор - Константинопольский'
                             ,
                             number_rules=8
                             ),
                PageTurnover(page=90
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Третий Вселенский Собор - Эфесский'
                             ,
                             # Послание записано как девятое правило
                             # **Не выделено как отдельная глава, вi(12) - уже про 4 Вселенский Собор**
                             number_rules=8
                             ),
                ),
    const_week_page=(1, 35)
    ,
    pdf_plus_pages=9
    ,
    pdf_path=Path(r"C:\Users\MaxDroN\pravoslavie\canons\kormchij\kormchaya_4.pdf")
)
