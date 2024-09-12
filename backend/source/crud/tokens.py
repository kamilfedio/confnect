from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from source.schemas.base import Base
from source.models.token import Token
from source.utils.enums import TokenType


async def create(model: Base, session: AsyncSession) -> Base:
    """
        create token in database
    Args:
        model (Base): token data object
        session (AsyncSession): current session

    Returns:
        Base: token object data
    """
    session.add(model)
    await session.commit()
    await session.refresh(model)

    return model


async def get_by_id(
    id: str, token_type: TokenType, session: AsyncSession
) -> Base | None:
    """
    get token by id and type
    Args:
        id (str): token id
        token_type (TokenType): token type
        session (AsyncSession): current session

    Returns:
        Base | None: token or none
    """
    query = select(Token).where(
        Token.token == id,
        Token.type == token_type,
        Token.expiration_date > datetime.now(),
    )
    res = await session.execute(query)
    return res.scalars().one_or_none()


async def get_user_tokens_by_id(
    user_id: int, token_type: TokenType, session: AsyncSession
) -> list[Base]:
    """
        get all user tokens by id and type
    Args:
        user_id (int): user id
        token_type (TokenType): token type
        session (AsyncSession): curreny session

    Returns:
        list[Base]: list of tokens data object
    """
    query = select(Token).where(Token.user_id == user_id, Token.type == token_type)
    res = await session.execute(query)
    return res.scalars().all()


async def disable_token(id: int, session: AsyncSession) -> None:
    """
    set token expirated on True
    Args:
        id (int): token id
        session (AsyncSession): current session
    """
    query = select(Token).where(Token.token == id)
    token: Token = await session.execute(query)
    if token:
        token.expirated = True
        await session.commit()
