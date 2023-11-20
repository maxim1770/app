from pathlib import Path

from app import enums
from ..object_storage import ObjectStorage


class _PrepareManuscriptPath(object):

    def __init__(self, path: Path, pdf_path: Path, *, object_storage: ObjectStorage):
        self.__path = path
        self.__pdf_path = pdf_path
        self.__object_storage = object_storage

    @property
    def path(self) -> Path:
        if self.__object_storage.is_folder(self.__path):
            raise FileExistsError(f'The Manuscript imgs dir {self.__path} is already exists')
        return self.__path

    @property
    def created_path(self) -> Path:
        if not self.__object_storage.is_folder(self.__path):
            raise FileNotFoundError(f'The Manuscripts imgs dir {self.__path} is not exists')
        return self.__path

    @property
    def pdf_path(self) -> Path:
        if not self.__object_storage.is_folder(self.__pdf_path.parent):
            raise FileNotFoundError(f'The Manuscript pdf {self.__pdf_path} path.parent is not exists')
        if self.__object_storage.get(self.__pdf_path):
            raise FileExistsError(f'The Manuscript pdf {self.__pdf_path} is already exists')
        return self.__pdf_path

    @property
    def created_pdf_path(self) -> Path:
        # if not self.__object_storage.get(self.__pdf_path):
        #     raise FileNotFoundError(f'The Manuscripts pdf {self.__pdf_path} is not exists')
        return self.__pdf_path


def replace_path_base_dir(
        path: Path,
        *,
        new: str = 'pdf',
        old: str = 'img'
) -> Path:
    return Path(str(path).replace(old, new))


class PrepareManuscriptPathFactory(object):
    _BASE_MANUSCRIPTS_DIR = Path('img') / 'manuscripts'

    @classmethod
    def from_lib(
            cls,
            *,
            fund_title: enums.FundTitle,
            library_title: enums.LibraryTitle,
            code: str,
            object_storage: ObjectStorage | None = None
    ) -> _PrepareManuscriptPath | Path:
        path: Path = cls._BASE_MANUSCRIPTS_DIR / library_title.name / fund_title.name / code
        pdf_path: Path = replace_path_base_dir(path).with_suffix('.pdf')
        if object_storage:
            return _PrepareManuscriptPath(path, pdf_path, object_storage=object_storage)
        else:
            return path

    @classmethod
    def from_lls(
            cls,
            *,
            code: str,
            object_storage: ObjectStorage | None = None
    ) -> _PrepareManuscriptPath | Path:
        path: Path = cls._BASE_MANUSCRIPTS_DIR / 'lls' / code
        pdf_path: Path = replace_path_base_dir(path).with_suffix('.pdf')
        if object_storage:
            return _PrepareManuscriptPath(path, pdf_path, object_storage=object_storage)
        else:
            return path
