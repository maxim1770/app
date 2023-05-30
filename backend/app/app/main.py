import logging

from fastapi import FastAPI
from fastapi_pagination import add_pagination
from sqladmin import Admin, ModelView
from starlette.middleware.cors import CORSMiddleware

from app import models
from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db.session import engine

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

app = FastAPI(title=settings.PROJECT_NAME)
admin = Admin(app, engine)

add_pagination(app)


class ManuscriptAdmin(ModelView, model=models.Manuscript):
    form_columns = [
        models.Manuscript.id,
        models.Manuscript.title,
        models.Manuscript.neb_slug,
        models.Manuscript.code_title,
        models.Manuscript.code,
        models.Manuscript.handwriting,
        models.Manuscript.not_numbered_pages,
        models.Manuscript.year,
        models.Manuscript.fund,
    ]
    column_list = [
        models.Manuscript.id,
        models.Manuscript.title,
        models.Manuscript.neb_slug,
        models.Manuscript.code_title,
        models.Manuscript.code,
        models.Manuscript.handwriting,
        models.Manuscript.not_numbered_pages,
        models.Manuscript.year,
        models.Manuscript.fund,
        # models.Manuscript.books
    ]
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True


admin.add_view(ManuscriptAdmin)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)

# def main():
#     uvicorn.run('main:app', reload=True, port=8001)  # debug=True)  # host="0.0.0.0", port=8000)
#
#
# if __name__ == '__main__':
#     main()
