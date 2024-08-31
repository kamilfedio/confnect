from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from source.schemas.base import Base
from source.models.invitation_code import InvitationCode

class CodesCrud:
    async def create(self, model: Base, session: AsyncSession) -> Base:
        session.add(model)
        await session.commit()
        await session.refresh(model)

        return model
    
    async def get_by_id(self, id: int, session: AsyncSession) -> Base | None:
        query = select(InvitationCode).where(InvitationCode.id == id)
        res = await session.execute(query)
        return res.scalars().one_or_none()
    
    async def get_by_code(self, code: str, session: AsyncSession) -> Base | None:
        query = select(InvitationCode).where(InvitationCode.code == code, InvitationCode.expiration_date > datetime.now())
        res = await session.execute(query)
        return res.scalars().one_or_none()
    
codes_crud = CodesCrud()
