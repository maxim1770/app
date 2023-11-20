import logging
from pathlib import Path

import boto3
from sqlalchemy.orm import Session

from app import crud, utils, models, schemas
from app.api import deps
from app.utils import ObjectStorage

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def calculate_manuscript_all_num_pages(
        object_storage: ObjectStorage,
        *,
        manuscript: models.Manuscript
) -> int:
    __manuscript_path: Path = utils.assemble_manuscript_path(manuscript)
    preview_imgs_path: Path = Path(str(__manuscript_path).replace('img', 'preview-img'))
    all_num_pages: int = len(object_storage.ls(preview_imgs_path))
    if all_num_pages == 1000:
        preview_imgs_path /= '1'
        all_num_pages += len(
            [
                preview_img_path for preview_img_path in object_storage.ls(preview_imgs_path)
                if len(preview_img_path.stem) > 3
            ]
        )
        all_num_pages -= 1
    return all_num_pages


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    boto_session: boto3.session.Session = next(deps.get_boto())
    object_storage = ObjectStorage(boto_session)

    for manuscript in crud.manuscript.get_all(db):
        all_num_pages: int = calculate_manuscript_all_num_pages(object_storage, manuscript=manuscript)
        if all_num_pages > 0:
            crud.manuscript.update(db, db_obj=manuscript, obj_in=schemas.ManuscriptUpdate(all_num_pages=all_num_pages))
