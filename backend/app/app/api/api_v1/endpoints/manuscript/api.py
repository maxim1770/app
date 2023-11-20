from fastapi import APIRouter

from app.api.api_v1.endpoints.manuscript import manuscripts
from ..manuscript import lls

manuscripts.router.include_router(lls.router, prefix='/lls')

router = APIRouter()

router.include_router(manuscripts.router)
