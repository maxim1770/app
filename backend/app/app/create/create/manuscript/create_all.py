from pathlib import Path

from sqlalchemy.orm import Session

from app import models, schemas, utils
from .manuscript import create_manuscript_bookmark
from ...prepare import prepare_manuscript_bookmark


def create_manuscript_bookmarks(
        db: Session,
        *,
        manuscript: models.Manuscript
) -> models.Manuscript:
    try:
        pdf_path: Path = utils.PrepareManuscriptPath(
            fund_title=manuscript.fund.title,
            library_title=manuscript.fund.library,
            code=manuscript.code,
        ).created_pdf_path
    except FileNotFoundError as e:
        raise ValueError(e.args[0])
    bookmarks_data_in: list[schemas.BookmarkDataCreate] = prepare_manuscript_bookmark(
        pdf_path=pdf_path,
        not_numbered_pages=manuscript.not_numbered_pages,
        from_neb=True if manuscript.neb_slug else False,
        first_page_position=manuscript.first_page_position
    )
    for bookmark_data_in in bookmarks_data_in:
        create_manuscript_bookmark(db, manuscript=manuscript, bookmark_data_in=bookmark_data_in)
    return manuscript
