from pathlib import Path

from sqlalchemy.orm import Session

from app import models, schemas
from .manuscript import create_manuscript_bookmark
from ...prepare import prepare_manuscript_bookmark


def create_manuscript_bookmarks(
        db: Session,
        *,
        manuscript: models.Manuscript
) -> models.Manuscript:
    pdf_path = Path(f'../../pravoslavie/lives_saints/prologs/{manuscript.neb_slug.replace("-", "_")}.pdf')
    from_neb: bool = True if manuscript.neb_slug else False
    bookmarks_data_in: list[schemas.BookmarkDataCreate] = prepare_manuscript_bookmark(
        pdf_path=pdf_path,
        not_numbered_pages=manuscript.not_numbered_pages,
        from_neb=from_neb,
        first_page_position=manuscript.first_page_position
    )
    for bookmark_data_in in bookmarks_data_in:
        create_manuscript_bookmark(db, manuscript=manuscript, bookmark_data_in=bookmark_data_in)
    return manuscript
