from pathlib import Path

from app import enums
from app.core.config import settings


class PrepareManuscriptPath(object):

    def __init__(
            self,
            *,
            fund_title: enums.FundTitle,
            library_title: enums.LibraryTitle,
            code: str,
    ):
        self.__path = Path(settings.DATA_DIR) / 'img' / 'manuscripts' / library_title.name / fund_title.name / code
        self.__pdf_path = Path(str(self.__path).replace('img', 'pdf')).with_suffix('.pdf')

    @property
    def path(self) -> Path:
        if not self.__path.parent.exists():
            raise FileNotFoundError(f'The Manuscript imgs dir {self.__path} path.parent is not exists')
        if self.__path.exists():
            raise FileExistsError(f'The Manuscript imgs dir {self.__path} is already exists')
        return self.__path

    @property
    def created_path(self) -> Path:
        if not self.__path.exists():
            raise FileNotFoundError(f'The Manuscripts imgs dir {self.__path} is not exists')
        return self.__path

    @property
    def pdf_path(self) -> Path:
        if not self.__pdf_path.parent.exists():
            raise FileNotFoundError(f'The Manuscript pdf {self.__pdf_path} path.parent is not exists')
        if self.__pdf_path.exists():
            raise FileExistsError(f'The Manuscript pdf {self.__pdf_path} is already exists')
        return self.__pdf_path

    @property
    def created_pdf_path(self) -> Path:
        if not self.__pdf_path.exists():
            raise FileNotFoundError(f'The Manuscripts pdf {self.__pdf_path} is not exists')
        return self.__pdf_path
