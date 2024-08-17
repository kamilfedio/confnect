from sqlalchemy import Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession

from source.schemas.form import FormRead
from source.models.form import Form
from source.schemas.base import Base

class FormsCrud:
    async def get_all(self, pagination: tuple[int, int], session: AsyncSession) -> Sequence[Base]:
        skip, limit = pagination
        query = select(Form).offset(skip).limit(limit)
        res = await session.execute(query)

        return res.scalars().all()

    async def get_by_id(self) -> Base:
        pass

    async def create(self, model: Base, session: AsyncSession) -> Base:
        new_model = Form(**model.model_dump())
        session.add(new_model)
        await session.commit()
        await session.refresh

        return new_model
