from sqlalchemy import Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession

from source.schemas.base import Base
from source.models.base import Base as BaseModel
from source.models.user import User


async def get_by_id(user_id: int, session: AsyncSession) -> Base | None:
    """
        get user by id
    Args:
        user_id (int): user id
        session (AsyncSession): current session

    Returns:
        Base | None: user or none
    """
    query = select(User).where(User.id == user_id)
    res = await session.execute(query)

    return res.scalars().one_or_none()


async def create(model: BaseModel, session: AsyncSession) -> Base:
    """
        create user in database
    Args:
        model (BaseModel): user data object
        session (AsyncSession): current session

    Returns:
        Base: user data object
    """
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model


async def update(model: Base, session: AsyncSession) -> Base:
    """
    update user in database
    Args:
        model (Base): user data update object
        session (AsyncSession): current session

    Returns:
        Base: user data updated object
    """
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model


async def get_by_email(email: str, session: AsyncSession) -> Base | None:
    """
    get user by email
    Args:
        email (str): user email
        session (AsyncSession): current session

    Returns:
        Base | None: user or none
    """
    query = select(User).where(User.email == email)
    res = await session.execute(query)

    return res.scalars().one_or_none()
