from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from ...core.security import get_password_hash, verify_password
from ..crud.base import CRUDBase
from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    @staticmethod
    async def get_by_email(db: AsyncSession, *, email: str) -> Optional[User]:
        p = select(User).filter(User.email == email)
        _ = await db.execute(p)
        return _.scalar()

    async def create(self, db: AsyncSession, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )

        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self, db: AsyncSession, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password

        return await super().update(db, db_obj=db_obj, obj_in=update_data)

    async def authenticate(self, db: AsyncSession, *, email: str, password: str) -> Optional[User]:
        user_ = await self.get_by_email(db, email=email)

        if not user_:
            return None
        if not verify_password(password, user_.hashed_password):
            return None

        return user_

    @staticmethod
    def is_active(user_: User) -> bool:
        return user_.is_active

    @staticmethod
    def is_superuser(user_: User) -> bool:
        return user_.is_superuser


user = CRUDUser(User)
