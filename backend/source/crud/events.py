from sqlalchemy import Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from source.models.base import Base
from source.models.event import Event


async def get_all(
    user_id: int, pagination: tuple[int, int], session: AsyncSession
) -> Sequence[Base]:
    """
    get all  user events
    Args:
        user_id (int): user id
        pagination (tuple[int, int]): pagination - offset&limit
        session (AsyncSession): current session

    Returns:
        Sequence[Base]: list of events data object
    """
    skip, limit = pagination
    query = select(Event).where(Event.user_id == user_id).offset(skip).limit(limit)
    res = await session.execute(query)

    return res.scalars().all()


async def get_by_id(id: int, session: AsyncSession) -> Base | None:
    """
    get event by id
    Args:
        id (int): event id
        session (AsyncSession): current session

    Returns:
        Base | None: event or none
    """
    query = select(Event).where(Event.id == id)
    res = await session.execute(query)

    return res.scalars().one_or_none()


async def create(model: Base, session: AsyncSession) -> Base:
    """
    create event in database
    Args:
        model (Base): event data object
        session (AsyncSession): current session

    Returns:
        Base: event data object
    """
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model


async def update(model: Base, session: AsyncSession) -> Base:
    """
    update event data in database
    Args:
        model (Base): event data updated object
        session (AsyncSession): current session

    Returns:
        Base: event data object
    """
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model


async def delete(id: int, session: AsyncSession) -> None:
    """
    delete event by id
    Args:
        id (int): event id
        session (AsyncSession): current session

    Raises:
        HTTPException: if event doesn't exists
    """
    query = select(Event).where(Event.id == id)
    res = await session.execute(query)
    model = res.scalars().one_or_none()

    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )

    session.delete(model)
    await session.commit()
