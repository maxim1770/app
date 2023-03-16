from pathlib import Path

from PIL import Image
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.core.config import settings

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    manuscript = crud.manuscript.get_by_code(db, code='50d07a48-b72e-4372-b020-ad5baf59f797')
    imgs_path: Path = Path(
        f'{settings.DATA_DIR}/img/manuscripts/{manuscript.fund.library.name}/{manuscript.fund.title.name}/{manuscript.code}'
    )
    if not imgs_path.exists():
        raise FileNotFoundError('manuscripts data is not exists')
    pdf_path = Path(str(imgs_path).replace('img', 'pdf') + '.pdf')
    imgs = [
        Image.open(imgs_path / f'{num + 1}.webp')
        for num in range(len(list(imgs_path.iterdir())))
    ]
    imgs[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=imgs[1:]
    )
