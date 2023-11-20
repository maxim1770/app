from pathlib import Path

from ..object_storage import ObjectStorage


class _PrepareIconPath(object):

    def __init__(
            self,
            path: Path,
            *,
            object_storage: ObjectStorage
    ):
        self.__path = path
        self.__object_storage = object_storage

    @property
    def path(self) -> Path:
        if self.__object_storage.get(self.__path):
            raise FileExistsError(f'The Icon img {self.__path} is already exists')
        return self.__path

    @property
    def created_path(self) -> Path:
        if not self.__object_storage.get(self.__path):
            raise FileNotFoundError(f'The Icons imgs dir {self.__path} is not exists')
        return self.__path


class PrepareIconPathFactory(object):
    _BASE_ICONS_DIR = Path('img') / 'icons'

    @classmethod
    def get(
            cls,
            *,
            pravicon_id: int,
            holiday_slug: str,
            object_storage: ObjectStorage,
    ) -> _PrepareIconPath:
        path: Path = cls._BASE_ICONS_DIR / holiday_slug / f'pravicon-{pravicon_id}.webp'
        return _PrepareIconPath(path, object_storage=object_storage)

    @classmethod
    def get_gallerix(
            cls,
            *,
            gallerix_id: int,
            holiday_slug: str,
            object_storage: ObjectStorage,
    ) -> _PrepareIconPath:
        path: Path = cls._BASE_ICONS_DIR / holiday_slug / f'gallerix-{gallerix_id}.webp'
        return _PrepareIconPath(path, object_storage=object_storage)

    @classmethod
    def get_shm(
            cls,
            *,
            shm_id: int,
            holiday_slug: str,
            object_storage: ObjectStorage,
    ) -> _PrepareIconPath:
        path: Path = cls._BASE_ICONS_DIR / holiday_slug / f'shm-{shm_id}.webp'
        return _PrepareIconPath(path, object_storage=object_storage)


