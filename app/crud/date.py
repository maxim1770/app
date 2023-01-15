from datetime import date as date_type

from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps
from app.db.session import engine, Base


def get_dates(db: Session, skip: int = 0, limit: int = 100) -> list[models.Date]:
    return db.query(models.Date).offset(skip).limit(limit).all()


def get_date(db: Session, date: date_type) -> models.Date | None:
    return db.query(models.Date).filter(models.Date.date == str(date)).first()


def create_date(db: Session, date: schemas.DateCreate) -> models.Date:
    db_date: models.Date = models.Date(**date.dict())
    db.add(db_date)
    db.commit()
    db.refresh(db_date)
    return db_date


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    Base.metadata.create_all(bind=engine)

    # date: schemas.DateCreate = schemas.DateCreate(
    #     date=date_type(2022, 8, 12)
    # )
    #
    # db_date: models.Date = models.Date(**date.dict())
    db_date: models.Date = get_date(db, date=date_type(2022, 8, 12))

    saint: schemas.SaintCreate = schemas.SaintCreate(
        name='тест 3',
        slug='test-3'
    )

    db_saint: models.Saint = models.Saint(
        **saint.dict()
    )

    # print(db_date.__dict__)
    # print(db_date._sa_instance_state.__dict__)
    # print("ffd", db_date.saints[0].__dict__)
    # print(db_date.saints.append(db_saint))
    # print(db_date.saints)

    print(db_date.__dict__)
    print(db_date._sa_instance_state.__dict__)

    print(db_date.saints)
    print(db_date.association_table)

    # db.add(db_date)
    # db.commit()
    # db.refresh(db_date)

    # print(db_saint.__dict__)
    # print(db_saint._sa_instance_state.__dict__)
