from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

from app.utils.cyrillic import Cyrillic
from app.utils.pages.books.neb.from_nlr.kormchaya_3 import bookmark_pages_turnover
from app.utils.pages.pages_turnover_models import get_pages_models
from app.utils.pages.schemes import ListPagesModel


def add_bookmarks(models: ListPagesModel):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(models.__root__[0].pdf_path)

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    for model in models.__root__:
        # Так же можно добавить число на дс, используя модифицированную библиотеку roman
        title: str = f'{Cyrillic.to_cyrillic(model.week_number)}({model.week_number}), {model.title}, Правил: {Cyrillic.to_cyrillic(model.number_rules)}({model.number_rules})'

        pdf_writer.add_bookmark(f'{title}', model.first_page + model.pdf_plus_pages)

    with models.__root__[0].pdf_path.open(mode="wb") as file_:
        pdf_writer.write(file_)


def main():
    path: Path = Path(r"C:\Users\MaxDroN\pravoslavie\canons\kormchij\kormchaya_3.pdf")
    pdf_plus_pages: int = 1  # для kormchaya_3

    add_bookmarks(path, get_pages_models(bookmark_pages_turnover), pdf_plus_pages)


if __name__ == '__main__':
    main()

# Пример того как делать вложенные закладки
# parent = pdf_writer.add_bookmark("Евангельские чтения", 5)  # add parent bookmark
# pdf_writer.add_bookmark("1 Неделя", 5, parent)  # add child bookmark
# pdf_writer.add_bookmark("2 Неделя", 6, parent)  # add child bookmark
# pdf_writer.add_bookmark("3 Неделя", 7, parent)  # add child bookmark
#
