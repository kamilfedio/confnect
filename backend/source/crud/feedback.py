from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from source.models.feedback import Feedback
from source.schemas.base import Base


async def create(model: Base, session: AsyncSession) -> Base:
    """
    create feedback in database
    Args:
        model (Base): feedback object data
        session (AsyncSession): current session

    Returns:
        Base: feedback data object
    """
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model


async def get_all(
    event_id: int, pagination: tuple[int, int], session: AsyncSession
) -> list[Base]:
    """
    get all feedbacks from event
    Args:
        event_id (int): event id
        pagination (tuple[int, int]): pagination - offset&limit
        session (AsyncSession): curreny session

    Returns:
        list[Base]: list of feedbacks
    """
    query = (
        select(Feedback)
        .where(Feedback.event_id == event_id)
        .limit(pagination[1])
        .offset(pagination[0])
    )
    res = await session.execute(query)
    return res.scalars().all()


async def get_by_id(id: int, session: AsyncSession) -> Base | None:
    """
    get feedback by id
    Args:
        id (int): feedback id
        session (AsyncSession): current session

    Returns:
        Base | None: feedback or none
    """
    query = select(Feedback).where(Feedback.id == id)
    res = await session.execute(query)
    return res.scalars().one_or_none()


async def delete_by_id(id: int, session: AsyncSession) -> None:
    """
    delete feedback from database
    Args:
        id (int): feedback id
        session (AsyncSession): current session
    """
    query = select(Feedback).where(Feedback.id == id)
    res = await session.execute(query)
    feedback = res.scalars().one_or_none()
    if feedback:
        session.delete(feedback)
        await session.commit()


async def get_all_user(
    user_id: int, pagination: tuple[int, int], session: AsyncSession
) -> list[Base]:
    """
    get all user feedbacks
    Args:
        user_id (int): user id
        pagination (tuple[int, int]): pagination - offset&limit
        session (AsyncSession): current session

    Returns:
        list[Base]: list of feedbacks
    """
    query = (
        select(Feedback)
        .where(Feedback.user_id == user_id)
        .limit(pagination[1])
        .offset(pagination[0])
    )
    res = await session.execute(query)
    return res.scalars().all()
