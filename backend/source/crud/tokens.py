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

tokens_crud = TokensCrud()
