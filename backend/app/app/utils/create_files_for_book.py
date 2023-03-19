import re
from abc import ABC
from pathlib import Path
from typing import Pattern

from pydantic import BaseModel, DirectoryPath, Field, constr


def copy_names_files():
    """
    код который перехонял файлы с docs/books в src/books, менял .md на .py
    и оставлял те же имена файлов

    Делал он это только для файлов books/rsl
    :return:
    """
    path_docs = Path('../../docs/books/rsl')

    path_src = Path('pages/books/rsl')

    for i in path_docs.iterdir():
        path = path_src.joinpath(i.name)
        path.mkdir(exist_ok=True)

        path.joinpath('__init__.py').touch(exist_ok=True)

        for j in path_docs.joinpath(i.name).iterdir():
            file_path = path.joinpath(j.stem).with_suffix(".py")
            file_path.touch(exist_ok=True)


def replace_dash_with_underscore(file_name: str) -> str:
    """
    Замена "-" на "_"
    """
    pattern: Pattern[str] = re.compile(r"-")
    string: str = file_name
    replace: str = "_"

    return re.sub(pattern, replace, string)


class LibBaseScheme(BaseModel, ABC):
    part_url_path_book: constr(regex=None)
    path_common: DirectoryPath
    text_for_name_folder: str = Field(default='', description="Нужно для rsl, добавляет rsl вначале имени фонда")


class NebScheme(LibBaseScheme):
    part_url_path_book: constr(
        regex=r"""(?x)     # Позволяет писать комментарии внутри рег. выр. Подробнее тут: https://stackoverflow.com/a/20669086/19440443
      (?<=^)            # Начало строки
      (?:[a-z0-9]+-?)+  # Повторяем символы [a-z0-9] 1 или больше раз, и если нужно вместе с "-". И все выражение повторяем 1 или больше раз
      (?=\b$)           # Конец строки, к тому же проверяем что перед концом строки стоит буква, а не "-"
     """)


class NebFromNlrScheme(NebScheme):
    path_common: DirectoryPath = Path('books/neb/from_nlr')


class NebFromRslScheme(NebScheme):
    path_common: DirectoryPath = Path('books/neb/from_rsl')


class RslScheme(LibBaseScheme):
    part_url_path_book: constr(
        regex=r"""(?x)             # Позволяет писать комментарии внутри рег. выр. Подробнее тут: https://stackoverflow.com/a/20669086/19440443
      (?<=^)
      (?:\d+(?:-i+)?)           # Проверка первой части - шифра: цифры, потом (тире с i одной или много) ИЛИ (ничего)
      /                         # Разделение пути в url
      (?:f-(?:\d+(?:i+)?)-\d+)  # Формат записи ед. хранения f-, потом так же как шифр, только без тире, после -\d
      /?                        # ТАК ЖЕ ВОЗМОЖЕН "/" В КОНЦЕ СТРОКИ, ДЛЯ УДОБСТВА, В pathlib он убирается и все ок, НО С str НУЖНО БЫТО ОСТОРОЖНЫМ
      (?=$)
     """)
    path_common: DirectoryPath = Path('books/rsl')
    text_for_name_folder: str = 'rsl'


class SectionScheme(BaseModel):
    name: DirectoryPath
    # TODO добавить reges в files_suffix, и изменить str на constr(regex=r"""...""")
    files_suffix: str = Field(default='',
                              description="Расширение для файлов в директории. Если указано '' (по умолчанию), "
                                          "значит без расширения. Н: .py .md ")


def create_book_files(lib_scheme: LibBaseScheme,
                      sections_schemes: list[SectionScheme] = (
                              SectionScheme(name='..\..\docs', files_suffix='.md'),
                              # SectionScheme(name='src', files_suffix='.py')
                      )
                      ) -> bool:
    last_part_path_book: str = lib_scheme.text_for_name_folder + replace_dash_with_underscore(
        lib_scheme.part_url_path_book)

    common_path_book: Path = lib_scheme.path_common.joinpath(last_part_path_book)

    for section_scheme in sections_schemes:
        completed_path_book: Path = section_scheme.name.joinpath(common_path_book).with_suffix(
            section_scheme.files_suffix)

        completed_path_book.parent.mkdir(exist_ok=True)
        completed_path_book.touch()

    return True


def main():
    create_book_files(NebFromNlrScheme(part_url_path_book="sbornik-slov-i-zhitiy-stati-iz-chetih-miney"))

    # create_book_files(RslScheme(part_url_path_book="100-ii/f-100ii-47"))

    pass


if __name__ == '__main__':
    main()
