"""
Страница закладок для рукописи [neb](https://lib-fond.ru/lib-rgb/304-i/f-304i-206/)

"""
from pathlib import Path

from app.utils.pages.schemes import BookmarkPagesTurnoverModel, PageTurnover

bookmark_pages: BookmarkPagesTurnoverModel = BookmarkPagesTurnoverModel(
    first_week_number=1
    ,
    meta_bookmarks=(PageTurnover(page=1
                                 ,
                                 title='Содержание'
                                 ),
                    )
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
                             ,
                             title='Седьмой Вселенский Собор - Никейский'
                             ,
                             number_rules=22
                             ),
                PageTurnover(page=169
                             ,
                             title='Поместный Собор - Константинопольский (двукратный)'
                             ,
                             number_rules=16
                             ),
                PageTurnover(page=172
                             ,
                             title='Поместный Собор - Константинопольский'
                             ,
                             number_rules=3
                             ),
                PageTurnover(page=172
                             ,
                             title='Правила святого Василия Великого от посланий к епископу Амфилохию Иконийскому, Диодору Тарскому, и к другим неким послания'
                             ,
                             number_rules=91
                             ),
                PageTurnover(page=196
                             ,
                             title='Святаго Василя о времени согрешающих вкратце'
                             ,
                             # Выделено в отдельную 20 главу.
                             number_rules=26
                             ),
                PageTurnover(page=197
                             ,
                             title='От книг Божественных повелении, Божественыя кончины, Иустинияна, различныя заповеди'
                             ,
                             number_rules=87
                             ),
                PageTurnover(page=215
                             ,
                             title='t_22'
                             ,
                             number_rules=100_22
                             ),
                PageTurnover(page=224
                             ,
                             title='t_23'
                             ,
                             number_rules=100_23
                             ),
                PageTurnover(page=230
                             ,
                             title='t_24'
                             ,
                             number_rules=100_24
                             ),
                PageTurnover(page=237
                             ,
                             title='t_25'
                             ,
                             number_rules=100_25
                             ),
                PageTurnover(page=244
                             ,
                             title='t_26'
                             ,
                             number_rules=100_26
                             ),
                PageTurnover(page=248
                             ,
                             title='t_27'
                             ,
                             number_rules=100_27
                             ),
                PageTurnover(page=249
                             ,
                             title='t_28'
                             ,
                             number_rules=100_28
                             ),
                PageTurnover(page=251
                             ,
                             title='t_29'
                             ,
                             number_rules=100_29
                             ),
                PageTurnover(page=251
                             ,
                             title='t_30'
                             ,
                             number_rules=100_30
                             ),
                ),
    const_week_page=(1, 27)
    ,
    pdf_plus_pages=4
    ,
    pdf_path=Path(r"C:\Users\MaxDroN\pravoslavie\canons\kormchij\f_304i_206.pdf")
)
