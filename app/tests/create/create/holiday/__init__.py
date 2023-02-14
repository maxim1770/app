from sqlalchemy.orm import Session

from app import create
from app.api import deps
from app.create.create.holiday.create_all import create_all_saints_holidays

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    create_all_saints_holidays(db)

    create.create_all_great_holidays(db)
    create.create_all_movable_saints_holidays(db)
    create.create_all_cathedrals_saints(db)
    create.create_any_holidays(db)
