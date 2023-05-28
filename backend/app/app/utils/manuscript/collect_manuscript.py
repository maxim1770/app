from pathlib import Path

from app import enums
from app.core.config import settings


class PrepareManuscriptPath(object):

    def __init__(self, path: Path, pdf_path: Path):
        self.__path = path
        self.__pdf_path = pdf_path

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


class PrepareManuscriptPathFactory(object):
    _BASE_MANUSCRIPTS_DIR = Path(settings.DATA_DIR) / 'img' / 'manuscripts'

    @classmethod
    def from_lib(
            cls,
            *,
            fund_title: enums.FundTitle,
            library_title: enums.LibraryTitle,
            code: str,
    ) -> PrepareManuscriptPath:
        path: Path = cls._BASE_MANUSCRIPTS_DIR / library_title.name / fund_title.name / code
        pdf_path: Path = Path(str(path).replace('img', 'pdf')).with_suffix('.pdf')
        return PrepareManuscriptPath(path, pdf_path)

    @classmethod
    def from_lls(
            cls,
            *,
            code: str
    ) -> PrepareManuscriptPath:
        path: Path = cls._BASE_MANUSCRIPTS_DIR / 'lls' / code
        pdf_path: Path = Path(str(path).replace('img', 'pdf')).with_suffix('.pdf')
        return PrepareManuscriptPath(path, pdf_path)
