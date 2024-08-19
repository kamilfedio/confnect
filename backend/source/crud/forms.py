from sqlalchemy import Sequence, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from source.crud.base import BaseCRUD
from source.models.form import Form
from source.schemas.base import Base

class FormsCrud(BaseCRUD):
    async def get_all(self, pagination: tuple[int, int], session: AsyncSession) -> Sequence[Base]:
        skip, limit = pagination
        query = select(Form).offset(skip).limit(limit)
        res = await session.execute(query)

        return res.scalars().all()

    async def get_by_id(self, id: int, session: AsyncSession) -> Base | None:
        query = select(Form).where(Form.id == id)
        res = await session.execute(query)

        return res.scalars().one_or_none()

    async def create(self, model: Base, session: AsyncSession) -> Base:
        new_model = Form(**model.model_dump())
        session.add(new_model)
        await session.commit()
        await session.refresh(new_model)

        return new_model

    async def update(self, model: Base, session: AsyncSession) -> Base:
        pass

    async def delete(self, id: int, session: AsyncSession) -> None:
        query = delete(Form).where(Form.id == id)
        await session.execute(query)
        await session.commit()

        return
    


crud = FormsCrud()
