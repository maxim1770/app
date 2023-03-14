from fastapi import APIRouter

from app.api.api_v1.endpoints.manuscript import manuscripts

router = APIRouter()

router.include_router(manuscripts.router)
