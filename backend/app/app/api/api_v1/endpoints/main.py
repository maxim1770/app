from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse, ORJSONResponse

from app import enums
from app.core.config import settings

router = APIRouter()


@router.get('/assets/{asset_path:path}', response_class=FileResponse)
def get_asset(asset_path: Path):
    return settings.DATA_DIR / asset_path


@router.get('/', response_class=ORJSONResponse)
def get_const_data():
    return ORJSONResponse(
        {
            'book_topics': [i[0].upper() + i[1:] for i in list(enums.BookTopic)]
        }
    )
