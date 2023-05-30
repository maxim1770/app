from typing import Any, Generic, Type, TypeVar

import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
FilterSchemaType = TypeVar("FilterSchemaType", bound=Filter)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType, FilterSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_multi_by_filter(self, db: Session, *, filter: FilterSchemaType) -> sa.Select:
        ...

    @staticmethod
    def _filtering_and_sorting_select(select: sa.Select, *, filter: FilterSchemaType) -> sa.Select:
        select: sa.Select = filter.filter(select)
        select: sa.Select = filter.sort(select)
        return select

    def get_multi(
            self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        return list(db.execute(sa.select(self.model).offset(skip).limit(limit)).scalars())

    def get_by_slug(self, db: Session, *, slug: str) -> ModelType | None:
        return db.execute(sa.select(self.model).filter_by(slug=slug)).scalar_one_or_none()

    def get(self, db: Session, *, id: int) -> ModelType | None:
        return db.execute(sa.select(self.model).filter_by(id=id)).scalar_one_or_none()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_with_any(self, db: Session, *, obj_in: CreateSchemaType, **kwargs) -> ModelType:
        ...

    @staticmethod
    def update(
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: UpdateSchemaType | dict[str, Any]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove_by_slug(self, db: Session, *, slug: str) -> ModelType:
        obj = db.execute(sa.select(self.model).filter_by(slug=slug)).scalar_one_or_none()
        db.delete(obj)
        db.commit()
        return obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.execute(sa.select(self.model).filter_by(id=id)).scalar_one_or_none()
        db.delete(obj)
        db.commit()
        return obj
