from sqlalchemy import Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from source.models.base import Base
from source.models.event import Event



async def get_all(user_id: int, pagination: tuple[int, int], session: AsyncSession) -> Sequence[Base]:
    skip, limit = pagination
    query = select(Event).where(Event.user_id == user_id).offset(skip).limit(limit)
    res = await session.execute(query)

    return res.scalars().all()

async def get_by_id(id: int, session: AsyncSession) -> Base | None:
    query = select(Event).where(Event.id == id)
    res = await session.execute(query)

    return res.scalars().one_or_none()

async def create(model: Base, session: AsyncSession) -> Base:
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model

async def update(model: Base, session: AsyncSession) -> Base:
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model

async def delete(id: int, session: AsyncSession) -> None:
    query = select(Event).where(Event.id == id)
    res = await session.execute(query)
    model = res.scalars().one_or_none()

    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

    session.delete(model)
    await session.commit()