from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

from app.utils.pages.pages_turnover_models import pages_models

path: Path = Path(r"C:\Users\MaxDroN\pravoslavie\canons\kormchij\kormchaya_3.pdf")

pdf_writer = PdfWriter()
reader = PdfReader(path)

for page in reader.pages:
    pdf_writer.add_page(page)

PDF_PLUS_PAGES = 1  # для kormchaya_3
for pages_model in pages_models.__root__:
    # Так же можно добавить число на дс, используя модифицированную библиотеку roman
    pdf_writer.add_bookmark(f"Глава {pages_model.week_number}", pages_model.first_page + PDF_PLUS_PAGES)

# Пример того как делать вложенные закладки
# parent = pdf_writer.add_bookmark("Евангельские чтения", 5)  # add parent bookmark
# pdf_writer.add_bookmark("1 Неделя", 5, parent)  # add child bookmark
# pdf_writer.add_bookmark("2 Неделя", 6, parent)  # add child bookmark
# pdf_writer.add_bookmark("3 Неделя", 7, parent)  # add child bookmark
#


with path.open(mode="wb") as file_:
    pdf_writer.write(file_)
