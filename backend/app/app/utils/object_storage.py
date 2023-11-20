import logging
from pathlib import Path
from typing import Any

import boto3

from app import enums
from app.core.config import settings


class ObjectStorage(object):

    def __init__(self, boto_session: boto3.session.Session):
        self.__s3 = boto_session.client(
            service_name='s3',
            endpoint_url='https://storage.yandexcloud.net',
        )
        self.__bucket_name: str = settings.OBJECT_STORAGE_BUCKET_NAME

    def ls(self, common_prefix_path: Path | str = '') -> list[Path]:
        list_objects_data: dict[str, Any] = self.__get_list_objects_data(common_prefix_path)
        if 'Contents' in list_objects_data:
            return [Path(object_['Key']) for object_ in list_objects_data['Contents']]
        return []

    def is_folder(self, common_prefix_path: Path | str = '') -> bool:
        list_objects_data: dict[str, Any] = self.__get_list_objects_data(common_prefix_path, max_length=1)
        logging.warning(common_prefix_path)
        if 'Contents' in list_objects_data:
            logging.warning('True')
            return True
        return False

    def is_object(
            self,
            object_path: Path,
    ) -> bool:
        try:
            object_: dict[str, Any] = self.__s3.get_object_attributes(
                Bucket=self.__bucket_name,
                Key=self.__path2object_storage_str_path(object_path),
                ObjectAttributes=['StorageClass']
            )
        except Exception as e:
            return False
        else:
            return True

    def get(
            self,
            object_path: Path,
            *,
            version_id: str | None = None
    ) -> dict[str, Any] | None:
        try:
            __extra_kwargs: dict[str, Any] = {}
            if version_id:
                __extra_kwargs |= {'VersionId': version_id}
            object_: dict[str, Any] = self.__s3.get_object(
                Bucket=self.__bucket_name,
                Key=self.__path2object_storage_str_path(object_path),
                **__extra_kwargs
            )
        except Exception:
            return None
        else:
            return object_

    def upload(
            self,
            *,
            file_path: Path,
            object_path: Path,
            object_storage_class: enums.ObjectStorageClass = enums.ObjectStorageClass.STANDARD
    ) -> None:
        self.__s3.upload_file(
            Filename=file_path,
            Bucket=self.__bucket_name,
            Key=self.__path2object_storage_str_path(object_path),
            ExtraArgs={
                'StorageClass': object_storage_class
            }
        )

    def delete(self, object_path: Path) -> None:
        self.__s3.delete_file(
            Bucket=self.__bucket_name,
            Key=self.__path2object_storage_str_path(object_path),
        )

    def download(self, object_path: Path) -> None:
        self.__s3.download_file(
            Bucket=self.__bucket_name,
            Key=self.__path2object_storage_str_path(object_path),
            Filename=self.__path2object_storage_str_path(object_path),
        )

    def __get_list_objects_data(
            self,
            common_prefix_path: Path | str = '',
            *,
            max_length: int = 1000
    ) -> dict[str, Any]:
        list_objects_data: dict[str, Any] = self.__s3.list_objects(
            Bucket=self.__bucket_name,
            Prefix=self.__path2object_storage_str_path(common_prefix_path),
            MaxKeys=max_length
        )
        return list_objects_data

    @staticmethod
    def __path2object_storage_str_path(path: Path | str) -> str:
        return str(path).replace('\\', '/')
