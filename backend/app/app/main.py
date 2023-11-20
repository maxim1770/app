import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_pagination import add_pagination
from redis import asyncio as aioredis

from app.api.api_v1.api import api_router
from app.core.config import settings

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

app = FastAPI(title=settings.PROJECT_NAME)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        'redis://',
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        encoding="utf8",
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

add_pagination(app)
app.include_router(api_router)
