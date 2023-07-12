"""
Страница закладок для рукописи [neb](https://kp.rusneb.ru/item/material/kormchaya-3)


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
    pages_list=(PageTurnover(page=19
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Правила святых Апостолов'
                             ,
                             number_rules=85
                             ),
                PageTurnover(page=28
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Святого Апостола Павла особно правил'
                             ,
                             number_rules=17
                             ),
                PageTurnover(page=29
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Того ж правила о усопших и властелех'
                             ,
                             number_rules=2
                             ),
                PageTurnover(page=29
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Первый Вселенский Собор - Никейский'
                             ,
                             number_rules=20
                             ),
                PageTurnover(page=34
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Анкирский'
                             ,
                             number_rules=25
                             ),
                PageTurnover(page=39
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Поместный Собор - Неокесарийский'
                             ,
                             number_rules=14
                             ),
                PageTurnover(page=40
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Гангрский'
                             ,
                             number_rules=19
                             ),
                PageTurnover(page=42
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Антиохийский'
                             ,
                             number_rules=25
                             ),
                PageTurnover(page=46
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Лаодикийский'
                             ,
                             number_rules=58
                             ),
                PageTurnover(page=52
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Второй Вселенский Собор - Константинопольский'
                             ,
                             number_rules=8
                             ),
                PageTurnover(page=54
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Третий Вселенский Собор - Эфесский'
                             ,
                             # "Того же собора послание сущим в Памфилии епископом Правило Ѳ(9)" - **записано как девятое правило**
                             # **Не выделено как отдельная глава, вi(12) - уже про 4 Вселенский Собор**
                             number_rules=8
                             ),
                PageTurnover(page=55
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Четвертый Вселенский Собор - Халкидонский'
                             ,
                             number_rules=30
                             ),
                PageTurnover(page=61
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Сардикийский'
                             ,
                             # **Так же пропущены правила иi(18) и к(20) - ничего не написано про это.**
                             number_rules=21
                             ),
                PageTurnover(page=65
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Поместный Собор - Карфагенский'
                             ,
                             # Последнее правило помечено как рлв(132), но раньше правило рлв(132) уже было,
                             # и перед последним правилом идет правило рлг(133).
                             # Так что скорее всего описка, потому что **текст правила совпадает с текстом правила рлд(134).**
                             number_rules=134
                             ),
                PageTurnover(page=86
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Шестой Вселенский Собор - Константинопольский, Трульский'
                             ,
                             number_rules=102
                             ),
                PageTurnover(page=118
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Седьмой Вселенский Собор - Никейский'
                             ,
                             number_rules=22
                             ),
                PageTurnover(page=127
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Константинопольский (двукратный)'
                             ,
                             number_rules=16
                             ),
                PageTurnover(page=129
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Поместный Собор - Константинопольский'
                             ,
                             number_rules=3
                             ),
                PageTurnover(page=130
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='Правила святого Василия Великого от посланий к епископу Амфилохию Иконийскому, Диодору Тарскому, и к другим неким послания'
                             ,
                             number_rules=91
                             ),
                PageTurnover(page=152
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='Святаго Василя о времени согрешающих вкратце'
                             ,
                             # Выделено в отдельную 20 главу.
                             number_rules=26
                             ),
                PageTurnover(page=153
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='От книг Божественных повелении, Божественыя кончины, Иустинияна, различныя заповеди'
                             ,
                             number_rules=87
                             ),
                PageTurnover(page=169
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='t_22'
                             ,
                             number_rules=100_22
                             ),
                PageTurnover(page=178
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_23'
                             ,
                             number_rules=100_23
                             ),
                PageTurnover(page=183
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='t_24'
                             ,
                             number_rules=100_24
                             ),
                PageTurnover(page=190
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='t_25'
                             ,
                             number_rules=100_25
                             ),
                PageTurnover(page=197
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_26'
                             ,
                             number_rules=100_26
                             ),
                PageTurnover(page=201
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_27'
                             ,
                             number_rules=100_27
                             ),
                PageTurnover(page=202
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_28'
                             ,
                             number_rules=100_28
                             ),
                PageTurnover(page=203
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='t_29'
                             ,
                             number_rules=100_29
                             ),
                PageTurnover(page=204
                             ,
                             turnover=TurnoverEnum.left
                             ,
                             title='t_30'
                             ,
                             number_rules=100_30
                             ),
                PageTurnover(page=204
                             ,
                             turnover=TurnoverEnum.right
                             ,
                             title='end'
                             ,
                             number_rules=0
                             ),
                ),
    const_week_page=(1, 19)
    ,
    pdf_plus_pages=1
    ,
    pdf_path=Path(r"C:\Users\MaxDroN\pravoslavie\canons\kormchij\kormchaya_3.pdf")
)
