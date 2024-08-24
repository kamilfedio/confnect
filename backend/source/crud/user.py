from sqlalchemy import Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession

from source.schemas.base import Base
from source.models.base import Base as BaseModel
from source.crud.base import BaseCRUD
from source.models.user import User


class UserCrud(BaseCRUD):
    async def get_all(self, pagination: tuple[int, int], session: AsyncSession) -> Sequence:
        pass

    async def get_by_id(self, id: int, session: AsyncSession) -> Base | None:
        query = select(User).where(User.id == id)
        res = await session.execute(query)

        return res.scalars().one_or_none()
    
    async def create(self, model: BaseModel, session: AsyncSession) -> Base:
        session.add(model)
        await session.commit()
        await session.refresh(model)

        return model
    
    async def update(self, model: Base, session: AsyncSession) -> Base:
        pass

    async def delete(self, id: int, session: AsyncSession) -> None:
        pass

    async def get_by_email(self, email: str, session: AsyncSession) -> Base | None:
        query = select(User).where(User.email == email)
        res = await session.execute(query)

        return res.scalars().one_or_none()


user_crud = UserCrud()