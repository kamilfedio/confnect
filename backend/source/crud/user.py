from sqlalchemy import Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession

from source.schemas.base import Base
from source.models.base import Base as BaseModel
from source.models.user import User


async def get_all(pagination: tuple[int, int], session: AsyncSession) -> Sequence:
    pass

async def get_by_id(id: int, session: AsyncSession) -> Base | None:
    query = select(User).where(User.id == id)
    res = await session.execute(query)

    return res.scalars().one_or_none()

async def create(model: BaseModel, session: AsyncSession) -> Base:
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model

async def update(model: Base, session: AsyncSession) -> Base:
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model

async def get_by_email(email: str, session: AsyncSession) -> Base | None:
    query = select(User).where(User.email == email)
    res = await session.execute(query)

    return res.scalars().one_or_none()

async def get_by_id(id: int, session: AsyncSession) -> Base | None:
    query = select(User).where(User.id == id)
    res = await session.execute(query)

    return res.scalars().one_or_none()
