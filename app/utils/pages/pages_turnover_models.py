from app.utils.pages.schemes import ListPagesModel, PagesModel, BookmarkPagesTurnoverModel

from app.utils.pages.books.neb.from_nlr.kormchaya_3 import bookmark_pages_turnover


def get_pages_models(bookmark_pages: BookmarkPagesTurnoverModel) -> ListPagesModel:
    pages_models = ListPagesModel(__root__=[])

    if bookmark_pages.const_week_page != (
            bookmark_pages.first_week_number, bookmark_pages.pages_list[0].page):
        raise ValueError("Проверь соотношение страниц и номеров недель!")

    for i in range(len(bookmark_pages.pages_list) - 1):

        if bookmark_pages.pages_list[i].turnover != None:
            """
            Арифметическая прогрессия (1, 3, 5, 7) 2n - 1 - это первая скобка
            Если страница левая, то отнимаем единицу => 2n - 2 => 2(n - 1), и получается Ар. прогр. (0, 2, 4, 6) - это первая скобка
            - (1 - bookmark_pages_turnover.pages_list[i].turnover)
            Если left, то bookmark_pages_turnover.pages_list[i].turnover == -1 и получается - 1 => 2n - 2 => 2(n - 1) =>
            Листы идут по четным числам и всегда это левые части на обороте листа
            Если right, то bookmark_pages_turnover.pages_list[i].turnover == 0 и получается - 0 =>
            Правые части на обороте листа
            """
            first_page = (2 * bookmark_pages.pages_list[i].page - 1) + bookmark_pages.pages_list[i].turnover
        first_page = bookmark_pages.pages_list[i].page

        pages_models.__root__.append(PagesModel(week_number=bookmark_pages.first_week_number + i
                                                ,
                                                first_page=first_page
                                                ,
                                                title=bookmark_pages.pages_list[i].title
                                                ,
                                                number_rules=bookmark_pages.pages_list[i].number_rules
                                                ,
                                                pdf_plus_pages=bookmark_pages.pdf_plus_pages
                                                ,
                                                pdf_path=bookmark_pages.pdf_path
                                                ),
                                     )

    return pages_models


def main():
    # Получить имя скрипта (без .py), из которого выполняется этот кот
    # Код ниже выдаст строку str: f_304i_206
    # {Path(__file__).stem}

    # with open(f'pages.json', 'w', encoding='utf-8') as f:
    #     json.dump(pages_models.dict(), f, indent=4, ensure_ascii=False)

    pages_models: ListPagesModel = get_pages_models(bookmark_pages_turnover)

    for i in pages_models.__root__:
        print(i)

if __name__ == '__main__':
    main()

