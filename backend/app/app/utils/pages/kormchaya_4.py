"""
Страница закладок для рукописи [neb](https://kp.rusneb.ru/item/material/kormchaya-4)

"""
from pathlib import Path

from app.utils.pages.schemes import BookmarkPagesTurnoverModel, PageTurnover, TurnoverEnum

bookmark_pages_turnover: BookmarkPagesTurnoverModel = BookmarkPagesTurnoverModel(
    first_week_number=1
    ,
    meta_bookmarks=(PageTurnover(page=1
                                 ,
                                 turnover=TurnoverEnum.right
                                 ,
                                 title='Содержание'
                                 ),
                    )
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
                PageTurnover(page=93
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Четвертый Вселенский Собор - Халкидонский'
                             ,
                             number_rules=30
                             ),
                PageTurnover(page=102
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Сардикийский'
                             ,
                             # **Так же пропущены правила иi(18) и к(20) - ничего не написано про это.**
                             number_rules=21
                             ),
                PageTurnover(page=107
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Карфагенский'
                             ,
                             number_rules=134
                             ),
                PageTurnover(page=133
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Шестой Вселенский Собор - Константинопольский, Трульский'
                             ,
                             number_rules=102
                             ),
                PageTurnover(page=161
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Седьмой Вселенский Собор - Никейский'
                             ,
                             number_rules=22
                             ),
                PageTurnover(page=169
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Поместный Собор - Константинопольский (двукратный)'
                             ,
                             # В тексте 17 правил
                             # В других рукописях выделено как толк. на 16 правило, или просто с красной буквы.
                             number_rules=17
                             ),
                PageTurnover(page=171
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Поместный Собор - Константинопольский'
                             ,
                             number_rules=3
                             ),
                PageTurnover(page=171
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Правила святого Василия Великого от посланий к епископу Амфилохию Иконийскому, Диодору Тарскому, и к другим неким послания'
                             ,
                             number_rules=91
                             ),
                PageTurnover(page=193
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Святаго Василя о времени согрешающих вкратце'
                             ,
                             # Выделено в отдельную 20 главу.
                             number_rules=26
                             ),
                PageTurnover(page=193
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='От книг Божественных повелении, Божественыя кончины, Иустинияна, различныя заповеди'
                             ,
                             number_rules=87
                             ),
                PageTurnover(page=210
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_22'
                             ,
                             number_rules=100_22
                             ),
                PageTurnover(page=219
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_23'
                             ,
                             number_rules=100_23
                             ),
                PageTurnover(page=224
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='t_24'
                             ,
                             number_rules=100_24
                             ),
                PageTurnover(page=231
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='t_25'
                             ,
                             number_rules=100_25
                             ),
                PageTurnover(page=237
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='t_26'
                             ,
                             number_rules=100_26
                             ),
                PageTurnover(page=241
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_27'
                             ,
                             number_rules=100_27
                             ),
                PageTurnover(page=242
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_28'
                             ,
                             number_rules=100_28
                             ),
                PageTurnover(page=243
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='t_29'
                             ,
                             number_rules=100_29
                             ),
                PageTurnover(page=0
                             ,
                             turnover=TurnoverEnum.left  # random
                             ,
                             title='t_30'
                             ,
                             number_rules=100_30
                             ),
                ),
    const_week_page=(1, 35)
    ,
    pdf_plus_pages=9
    ,
    pdf_path=Path(r"C:\Users\MaxDroN\pravoslavie\canons\kormchij\kormchaya_4.pdf")
)
