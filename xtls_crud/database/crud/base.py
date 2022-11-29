from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from sqlalchemy.future import select
from sqlalchemy import desc

from ..db.base_class import Base
from ..db.session import SessionLocal as _session  # noqa

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
FilterType = TypeVar("FilterType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
        self.session = _session

    async def get(self, id: Any) -> Optional[ModelType]:
        _ = await self.session.execute(select(self.model).where(self.model.id == id))
        return _.scalar()

    async def get_multi_filter(
            self, *, filters: FilterType, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        if isinstance(filters, dict):
            filter_data = filters
        else:
            filter_data = filters.dict(exclude_unset=True)

        where = []
        for k, v in filter_data.items():
            if v:
                where.append(getattr(self.model, k) == v)

        query = select(self.model).where(*where).offset(skip).limit(limit)

        _ = await self.session.execute(query)
        return _.scalars().all()

    async def get_multi(
            self, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        _ = await self.session.execute(select(self.model).offset(skip).limit(limit).order_by(desc(self.model.id)))
        return _.scalars().all()

    async def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)

        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)

        return db_obj

    async def update(
            self,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)

        return db_obj

    async def remove(self, *, id: int) -> ModelType:
        obj = await self.session.execute(select(self.model).where(self.model.id == id))
        obj = obj.get(id)

        await self.session.delete(obj)
        await self.session.commit()

        return obj
