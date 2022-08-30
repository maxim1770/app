"""
Страница закладок для рукописи [neb](https://kp.rusneb.ru/item/material/kormchaya-3)


"""

from crs.schemes import BookmarkPagesTurnoverModel, PageTurnover, TurnoverEnum

bookmark_pages_turnover: BookmarkPagesTurnoverModel = BookmarkPagesTurnoverModel(
    first_week_number=1,
    pages_list=(PageTurnover(page=19
                             ,
                             turnover=TurnoverEnum.left
                             ),
                PageTurnover(page=28
                             ,
                             turnover=TurnoverEnum.right
                             ),
                PageTurnover(page=
                             ,
                             turnover=TurnoverEnum.
                             ),
                PageTurnover(page=
                             ,
                             turnover=TurnoverEnum.
                             ),
                PageTurnover(page=
                             ,
                             turnover=TurnoverEnum.
                             ),
                PageTurnover(page=
                             ,
                             turnover=TurnoverEnum.
                             ),
                PageTurnover(page=
                             ,
                             turnover=TurnoverEnum.
                             ),
                ),
    const_week_page=(1, 180)
)

print(bookmark_pages_turnover)
