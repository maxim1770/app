from sqlalchemy.orm import Session

from app.api import deps
from app.create.create.holiday.create_all import create_all_saints_holidays

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    create_all_saints_holidays(db)
