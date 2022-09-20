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
                PageTurnover(page=100
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Четвертый Вселенский Собор - Халкидонский'
                             ,
                             number_rules=30
                             ),
                PageTurnover(page=110
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Сардикийский'
                             ,
                             # **Так же пропущены правила иi(18) и к(20) - ничего не написано про это.**
                             number_rules=21
                             ),
                PageTurnover(page=116
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Карфагенский'
                             ,
                             number_rules=134
                             ),
                PageTurnover(page=145
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Шестой Вселенский Собор - Константинопольский, Трульский'
                             ,
                             number_rules=102
                             ),
                PageTurnover(page=176
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Седьмой Вселенский Собор - Никейский'
                             ,
                             # А в заглавии написано, что 20 правил, но в тексте 22.
                             number_rules=22
                             ),
                PageTurnover(page=185
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Поместный Собор - Константинопольский (двукратный)'
                             ,
                             # В тексте 17 правил
                             # В других рукописях выделено как толк. на 16 правило, или просто с красной буквы.
                             number_rules=17
                             ),
                PageTurnover(page=187
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Константинопольский'
                             ,
                             number_rules=3
                             ),
                PageTurnover(page=188
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Правила святого Василия Великого от посланий к епископу Амфилохию Иконийскому, Диодору Тарскому, и к другим неким послания'
                             ,
                             number_rules=91
                             ),
                PageTurnover(page=211
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Святаго Василя о времени согрешающих вкратце'
                             ,
                             # Выделено в отдельную 21 главу.
                             number_rules=26
                             ),
                PageTurnover(page=212
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='От книг Божественных повелении, Божественыя кончины, Иустинияна, различныя заповеди'
                             ,
                             number_rules=87
                             ),
                PageTurnover(page=229
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_22'
                             ,
                             number_rules=100_22
                             ),
                PageTurnover(page=238
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             # глава 24
                             title='t_24_moses'
                             ,
                             # number_rules=100_23
                             ),
                PageTurnover(page=249
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             # глава 25, но совпадает с главой 23 других рукописей
                             title='t_23'
                             ,
                             number_rules=100_23
                             ),
                PageTurnover(page=
                             ,
                             turnover=TurnoverEnum.
                             ,
                             # глава 26, но совпадает с главой 30 других рукописей
                             title='t_30'
                             ,
                             number_rules=100_30
                             ),
                ),
    const_week_page=(1, 41)
    ,
    pdf_plus_pages=7
    ,
    pdf_path=Path(r"C:\Users\MaxDroN\pravoslavie\canons\kormchij\kormchaya_pisec_sava_danilo.pdf")
)
