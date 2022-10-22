import uvicorn

from fastapi import FastAPI

from app.api.api_v1.api import api_router

app = FastAPI()

app.include_router(api_router)


def main():
    uvicorn.run('main:app', reload=True)


if __name__ == '__main__':
    main()
