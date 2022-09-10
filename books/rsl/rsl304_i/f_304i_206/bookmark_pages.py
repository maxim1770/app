"""
Страница закладок для рукописи [neb](https://lib-fond.ru/lib-rgb/304-i/f-304i-206/)

"""
from pathlib import Path

from crs.schemes import BookmarkPagesTurnoverModel, PageTurnover

bookmark_pages: BookmarkPagesTurnoverModel = BookmarkPagesTurnoverModel(
    first_week_number=1
    ,
    pages_list=(PageTurnover(page=27
                             ,
                             title='Правила святых Апостолов'
                             ,
                             number_rules=85
                             ),
                PageTurnover(page=42
                             ,
                             title='Святого Апостола Павла особно правил'
                             ,
                             number_rules=17
                             ),
                PageTurnover(page=43
                             ,
                             title='Того ж правила о усопших и властелех'
                             ,
                             # Выделены в отдельную главу
                             number_rules=2
                             ),
                PageTurnover(page=44
                             ,
                             title='Первый Вселенский Собор - Никейский'
                             ,
                             number_rules=20
                             ),
                PageTurnover(page=51
                             ,
                             title='Поместный Собор - Анкирский'
                             ,
                             number_rules=25
                             ),
                PageTurnover(page=59
                             ,
                             title='Поместный Собор - Неокесарийский'
                             ,
                             number_rules=14
                             ),
                PageTurnover(page=62
                             ,
                             title='Поместный Собор - Гангрский'
                             ,
                             number_rules=19
                             ),
                PageTurnover(page=65
                             ,
                             title='Поместный Собор - Антиохийский'
                             ,
                             number_rules=25
                             ),
                PageTurnover(page=72
                             ,
                             title='Поместный Собор - Лаодикийский'
                             ,
                             number_rules=58
                             ),
                PageTurnover(page=81
                             ,
                             title='Второй Вселенский Собор - Константинопольский'
                             ,
                             number_rules=8
                             ),
                PageTurnover(page=84
                             ,
                             title='Третий Вселенский Собор - Эфесский'
                             ,
                             # **Так же послание записано как девятое правило**
                             # **Не выделено как отдельная глава, вi(12) - уже про 4 Вселенский Собор**
                             number_rules=8
                             ),
                PageTurnover(page=86
                             ,
                             title='Четвертый Вселенский Собор - Халкидонский'
                             ,
                             number_rules=30
                             ),
                PageTurnover(page=97
                             ,
                             title='Поместный Собор - Сардикийский'
                             ,
                             # **Пропущены правила иi(18) и к(20) - написано, что этих правил нет.**
                             number_rules=21
                             ),
                PageTurnover(page=102
                             ,
                             title='Поместный Собор - Карфагенский'
                             ,
                             number_rules=134
                             ),
                PageTurnover(page=129
                             ,
                             title='Шестой Вселенский Собор - Константинопольский, Трульский'
                             ,
                             number_rules=102
                             ),
                PageTurnover(page=160
                             # ,
                             # title=''
                             # ,
                             # number_rules=
                             ),
                PageTurnover(page=169
                             # ,
                             # title=''
                             # ,
                             # number_rules=
                             ),
                PageTurnover(page=172
                             # ,
                             # title=''
                             # ,
                             # number_rules=
                             ),
                PageTurnover(page=196
                             # ,
                             # title=''
                             # ,
                             # number_rules=
                             ),
                PageTurnover(page=197
                             # ,
                             # title=''
                             # ,
                             # number_rules=
                             ),
                ),
    const_week_page=(1, 27)
    ,
    pdf_plus_pages=4
    ,
    pdf_path=Path(r"C:\Users\MaxDroN\pravoslavie\canons\kormchij\f_304i_206.pdf")
)
