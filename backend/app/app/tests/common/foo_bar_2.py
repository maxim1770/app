from sqlalchemy.orm import Session

from app import crud, utils
from app.api import deps

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    for saint in crud.saint.get_all(db):
        saint_name = saint.name
        saint_name = saint_name.replace('G_M_2', '').replace('G_M_1', '').replace('NEW', '').replace('G_Y_1', '')
        saint_name = utils.clean_extra_spaces(saint_name)
        saint_name = utils.set_first_letter_upper(saint_name)
        if saint_name != saint.name:
            print(saint_name)
            saint.name = saint_name
            db.add(saint)
            db.commit()
            db.refresh(saint)
