from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from source.schemas.base import Base
from source.models.token import Token
from source.utils.enums import TokenType

class TokensCrud:
    async def create(self, model: Base, session: AsyncSession) -> Base:
        session.add(model)
        await session.commit()
        await session.refresh(model)

        return model
    
    async def get_by_id(self, id: str, token_type: TokenType, session: AsyncSession) -> Base | None:
        query = select(Token).where(Token.token == id, Token.type == token_type, Token.expiration_date > datetime.now())
        res = await session.execute(query)
        return res.scalars().one_or_none()    
    
    async def get_user_tokens_by_id(self, user_id: int, token_type: TokenType, session: AsyncSession) -> list[Base]:
        query = select(Token).where(Token.user_id == user_id, Token.type == token_type)
        res = await session.execute(query)
        return res.scalars().all()

    async def disable_token(self, id: int, session: AsyncSession) -> None:
        query = select(Token).where(Token.token == id)
        token: Token = await session.execute(query)
        token.expirated = True

tokens_crud = TokensCrud()
