from pathlib import Path

from app.core.config import settings


class PrepareIconPath(object):

    def __init__(self, path: Path, pdf_path: Path):
        self.__path = path
        self.__pdf_path = pdf_path

    @property
    def path(self) -> Path:
        if not self.__path.parent.exists():
            raise FileNotFoundError(f'The Icon imgs dir {self.__path} path.parent is not exists')
        if self.__path.exists():
            raise FileExistsError(f'The Icon imgs dir {self.__path} is already exists')
        return self.__path

    @property
    def path_two_parent(self) -> Path:
        if not self.__path.parent.parent.exists():
            raise FileNotFoundError(f'The Icon img base dir {self.__path} path.parent.parent is not exists')
        if self.__path.exists():
            raise FileExistsError(f'The Icon img {self.__path} is already exists')
        return self.__path

    @property
    def created_path(self) -> Path:
        if not self.__path.exists():
            raise FileNotFoundError(f'The Icons imgs dir {self.__path} is not exists')
        return self.__path

    @property
    def pdf_path(self) -> Path:
        if not self.__pdf_path.parent.exists():
            raise FileNotFoundError(f'The Icon pdf {self.__pdf_path} path.parent is not exists')
        if self.__pdf_path.exists():
            raise FileExistsError(f'The Icon pdf {self.__pdf_path} is already exists')
        return self.__pdf_path

    @property
    def created_pdf_path(self) -> Path:
        if not self.__pdf_path.exists():
            raise FileNotFoundError(f'The Icons pdf {self.__pdf_path} is not exists')
        return self.__pdf_path


class PrepareIconPathFactory(object):
    _BASE_MANUSCRIPTS_DIR = Path(settings.DATA_DIR) / 'img' / 'icons'

    @classmethod
    def get(
            cls,
            *,
            pravicon_id: int,
            holiday_slug: str
    ) -> PrepareIconPath:
        path: Path = cls._BASE_MANUSCRIPTS_DIR / holiday_slug / f'pravicon-{pravicon_id}'
        path: Path = path.with_suffix('.webp')
        pdf_path: Path = Path(str(path).replace('img', 'pdf')).with_suffix('.pdf')
        return PrepareIconPath(path, pdf_path)

    @classmethod
    def get_gallerix(
            cls,
            *,
            gallerix_id: int,
            holiday_slug: str
    ) -> PrepareIconPath:
        path: Path = cls._BASE_MANUSCRIPTS_DIR / holiday_slug / f'gallerix-{gallerix_id}'
        path: Path = path.with_suffix('.webp')
        pdf_path: Path = Path(str(path).replace('img', 'pdf')).with_suffix('.pdf')
        return PrepareIconPath(path, pdf_path)

    @classmethod
    def get_shm(
            cls,
            *,
            shm_id: int,
            holiday_slug: str
    ) -> PrepareIconPath:
        path: Path = cls._BASE_MANUSCRIPTS_DIR / holiday_slug / f'shm-{shm_id}'
        path: Path = path.with_suffix('.webp')
        pdf_path: Path = Path(str(path).replace('img', 'pdf')).with_suffix('.pdf')
        return PrepareIconPath(path, pdf_path)
