import boto3
from sqlalchemy.orm import Session

from app.api import deps
from app.create.prepare.manuscript.bookmark.create_pdf_bookmark import create_psaltyr_pdf_bookmarks

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    boto_session: boto3.session.Session = next(deps.get_boto())
    # create_all_cathedral_books(db)
    # create_all_psaltyr_books(db)
    create_psaltyr_pdf_bookmarks(db, boto_session=boto_session)
