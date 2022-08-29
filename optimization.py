"""
Тут данные для закладок рукописи: Евангелие учительское, которое я часто читаю
"""

from crs.schemes import BookmarkPagesModel


data_model = BookmarkPagesModel(
    first_week_number=1,
    pages_list=(180, 187, 192, 199, 207, 215, 223, 231, 236, 244, 252, 259, 265, 269,
                275, 281, 287, 294, 300,
                308, 313, 322, 332, 339,
                345, 354, 362, 369, 376,
                383, 391, 397, 405
                ),
    const_week_page=(1, 180)
)
