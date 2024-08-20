from sqlalchemy import Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession

from source.schemas.base import Base
from source.crud.base import BaseCRUD
from source.models.user import User


class UserCrud(BaseCRUD):
    async def get_all(self, pagination: tuple[int, int], session: AsyncSession) -> Sequence:
        pass

    async def get_by_id(self, id: int, session: AsyncSession) -> Base | None:
        query = select(User).where(User.id == id)
        res = await session.execute(query)

        return res.scalars().one_or_none()
    
    async def create(self, model: Base, session: AsyncSession) -> Base:
        new_model = User(**model.model_dump())
        session.add(new_model)
        await session.commit()
        await session.refresh(new_model)

        return new_model
    
    async def update(self, model: Base, session: AsyncSession) -> Base:
        pass

    async def delete(self, id: int, session: AsyncSession) -> None:
        pass


user_crud = UserCrud()