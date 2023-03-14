import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, schemas, enums


def get_funds(db: Session, skip: int = 0, limit: int = 100) -> list[models.Fund]:
    return db.query(models.Fund).offset(skip).limit(limit).all()


def get_fund(db: Session, *, title: enums.FundTitle) -> models.Fund | None:
    return db.execute(sa.select(models.Fund).filter_by(title=title)).scalar_one_or_none()


def create_fund(db: Session, *, fund_in: schemas.FundCreate) -> models.Fund:
    db_fund = models.Fund(**fund_in.dict())
    db.add(db_fund)
    db.commit()
    db.refresh(db_fund)
    return db_fund
