import logging
from pathlib import Path

import boto3
from PIL import Image, UnidentifiedImageError

from app import enums, utils
from app.api import deps
from app.utils import ObjectStorage

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def object_storage_upload_all_local_data_imgs(boto_session: boto3.session.Session) -> None:
    object_storage = ObjectStorage(boto_session)
    for file_path in Path(r"C:\Users\MaxDroN\python_projects\data\img").rglob('*.webp'):
        object_storage.upload(
            object_path=Path(str(file_path).split('data\\')[1]),
            file_path=file_path,
            object_storage_class=enums.ObjectStorageClass.STANDARD
        )
        logging.info('Upload ' + str(Path(str(file_path).split('data\\')[1])))


def __create_preview_img(img_path: Path, *, MAX_SIZE: tuple[int, int]) -> Image:
    img = Image.open(img_path)
    img.thumbnail(MAX_SIZE)
    return img


def __upload_img(object_storage: ObjectStorage, *, img: Image, object_path: Path) -> None:
    __temp_file_path = Path('some_img.webp')
    img.save(__temp_file_path, format='webp')
    object_storage.upload(
        file_path=__temp_file_path,
        object_path=object_path,
        object_storage_class=enums.ObjectStorageClass.STANDARD
    )
    __temp_file_path.unlink()


def object_storage_upload_all_preview_imgs(boto_session: boto3.session.Session) -> None:
    MAX_SIZE: tuple[int, int] = (350, 450)
    object_storage = ObjectStorage(boto_session)
    for file_path in Path(r"C:\Users\MaxDroN\python_projects\data\img").rglob('*.webp'):
        object_path: Path = utils.replace_path_base_dir(
            Path(str(file_path).split('data\\')[1]),
            new='preview-img'
        )
        if object_storage.get(object_path):
            logging.warning(f'Already {object_path}')
            continue
        try:
            img: Image = __create_preview_img(file_path, MAX_SIZE=MAX_SIZE)
        except UnidentifiedImageError:
            logging.error(file_path)
            continue
        else:
            __upload_img(object_storage, img=img, object_path=object_path)
            logging.warning(f'upload {object_path}')


if __name__ == '__main__':
    boto_session: boto3.session.Session = next(deps.get_boto())
    # object_storage_upload_all_local_data_imgs(boto_session)
    # object_storage_upload_all_preview_imgs(boto_session)

    # object_storage = ObjectStorage(boto_session)
    # object_storage.upload(
    #     object_path=Path(".well-known/acme-challenge/RBUCwd1ei7KFGEwkAmQkh1IteBDYi5QKyyfF21n1k_Q"),
    #     file_path=r"C:\Users\MaxDroN\Desktop\.well-known.txt",
    #     object_storage_class=enums.ObjectStorageClass.STANDARD
    # )

    # session = next(deps.get_session())

    # img = CollectIcon.collect_img(session,
    #                               img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLm3Yps2A-P5lA9pL7O6Y_lSLbMyEND6FW45k2pMkY-A&s')
    # path = Path('some_img.webp')
    # img.save(path, format='webp')
    #
    # # object_storage.upload(path.name)
    # path.unlink()

    # print(str(Path(r'img/icons')))
    # obj = object_storage.is_folder(common_prefix_path=Path(r'img/icons/ddsf'))
    # print(obj)
    # print(type(obj))

    # object_storage.ls('img/icons/den-pamjati-nazarij-rimljanin-i-gervasij-mediolanskij-i-protasij-mediolanskij-i-kelsij-mediolanskij/')

    # object_ = object_storage.is_object(
    #     object_path=Path('pdf/manuscripts/rsl/f_113/f-113-629.pdf'),
    #     # version_id='000602F47618DEE0'
    # )
    # print(object_)

    # temp_file = tempfile.TemporaryFile()
    # with io.FileIO(temp_file, 'w') as file:
    #     for b in obj['Body']._raw_stream:
    #         file.write(b)
