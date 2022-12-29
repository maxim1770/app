import json
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


pdf_writer = PdfWriter()
reader = PdfReader(
    r"C:\Users\MaxDroN\Desktop\Кормчая 16в(2).pdf")

for page in reader.pages:
    pdf_writer.add_page(page)

with Path(r'docs/books/rsl/rsl304_i/f_304i_206/data/pages.json').open(mode="r") as file:
    data = json.load(file)


# pages_model = ListPagesModel(__root__=data['__root__']) # Аналогичный код
pages_models = ListPagesModel(**data)

PDF_PLUS_PAGES = 4
for pages_model in pages_models.__root__:
    # Так же можно добавить число на дс, используя модифицированную библиотеку roman
    pdf_writer.add_bookmark(f"Глава {pages_model.week_number}", pages_model.first_page + PDF_PLUS_PAGES)


# Пример того как делать вложенные закладки
# parent = pdf_writer.add_bookmark("Евангельские чтения", 5)  # add parent bookmark
# pdf_writer.add_bookmark("1 Неделя", 5, parent)  # add child bookmark
# pdf_writer.add_bookmark("2 Неделя", 6, parent)  # add child bookmark
# pdf_writer.add_bookmark("3 Неделя", 7, parent)  # add child bookmark
#


with Path(r'C:\Users\MaxDroN\Desktop\Кормчая 16в(2)_bookmark.pdf').open(mode="wb") as file:
    pdf_writer.write(file)
