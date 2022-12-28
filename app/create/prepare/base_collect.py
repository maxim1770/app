from pathlib import Path

from bs4 import BeautifulSoup
from bs4.element import Tag


def collect_table(
        path_to_index: Path = Path(r'C:\Users\MaxDroN\python_projects\const_data_books\data\index.html')) -> Tag:
    # TODO: Насчет пути по умолчанию СКОРЕЕ ВСЕГО НЕПРАВИЛЬНО
    """
    :param path_to_index:
    """
    src: str = path_to_index.read_text(encoding="utf-8")

    soup: BeautifulSoup = BeautifulSoup(src, "lxml")

    table: Tag = soup.find("table", class_="adaptive").find("tbody")

    return table
