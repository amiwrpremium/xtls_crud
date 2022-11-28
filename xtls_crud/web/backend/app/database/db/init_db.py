from sqlalchemy.ext.asyncio import AsyncSession


from .. import crud, schemas
from ...core.settings import settings


async def init_db(db: AsyncSession) -> None:
    user = await crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)

    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = await crud.user.create(db, obj_in=user_in)

        return user


if __name__ == '__main__':
    import asyncio
    from .session import SessionLocal

    asyncio.run(init_db(SessionLocal()))
