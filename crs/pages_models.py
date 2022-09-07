# import json
#
# from crs.schemes import ListPagesModel, PagesModel
#
# from books.neb.from_nlr.kormchaya_4.bookmark_pages import bookmark_pages
#
# pages_models = ListPagesModel(__root__=[])
#
# if bookmark_pages.const_week_page != (bookmark_pages.first_week_number, bookmark_pages.pages_list[0]):
#     raise ValueError("Проверь соотношение страниц и номеров недель!")
#
# for i in range(len(bookmark_pages.pages_list) - 1):
#     pages_models.__root__.append(PagesModel(week_number=bookmark_pages.first_week_number + i
#                                             ,
#                                             first_page=bookmark_pages.pages_list[i]
#                                             ,
#                                             last_page=bookmark_pages.pages_list[i + 1]
#                                             ),
#                                  )
#
# if __name__ == '__main__':
#     # Получить имя скрипта (без .py), из которого выполняется этот кот
#     # Код ниже выдаст строку str: f_304i_206
#     # {Path(__file__).stem}
#     with open(f'pages.json', 'w', encoding='utf-8') as f:
#         json.dump(pages_models.dict(), f, indent=4, ensure_ascii=False)
