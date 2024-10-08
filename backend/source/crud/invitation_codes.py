from datetime import datetime
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from source.schemas.base import Base
from source.models.invitation_code import InvitationCode


async def create(model: Base, session: AsyncSession) -> Base:
    """
        create code in database
    Args:
        model (Base): code data object
        session (AsyncSession): async session

    Returns:
        Base: code object data
    """
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model


async def get_by_id(code_id: int, session: AsyncSession) -> Base | None:
    """
    get code by id
    Args:
        code_id (int): code id
        session (AsyncSession): current session

    Returns:
        Base | None: code or none
    """
    query = select(InvitationCode).where(InvitationCode.id == code_id)
    res = await session.execute(query)
    return res.scalars().one_or_none()


async def get_by_code(code: str, session: AsyncSession) -> Base | None:
    """
    get code object by code
    Args:
        code (str): code
        session (AsyncSession): current session

    Returns:
        Base | None: code object or none
    """
    query = select(InvitationCode).where(
        InvitationCode.code == code, InvitationCode.expiration_date > datetime.now()
    )
    res = await session.execute(query)
    return res.scalars().one_or_none()
