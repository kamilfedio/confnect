from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from source.models.feedback import Feedback
from source.schemas.base import Base

class FeedbacksCrud:
    async def create(self, model: Base, session: AsyncSession) -> Base:
        session.add(model)
        await session.commit()
        await session.refresh(model)

        return model
    
    async def get_all(self, event_id: int, pagination: tuple[int, int], session: AsyncSession) -> list[Base]:
        query = select(Feedback).where(Feedback.event_id == event_id).limit(pagination[1]).offset(pagination[0])
        res = await session.execute(query)
        return res.scalars().all()
    
    async def get_by_id(self, id: int, session: AsyncSession) -> Base | None:
        query = select(Feedback).where(Feedback.id == id)
        res = await session.execute(query)
        return res.scalars().one_or_none()
    
    async def delete_by_id(self, id: int, session: AsyncSession) -> None:
        query = select(Feedback).where(Feedback.id == id)
        res = await session.execute(query)
        feedback = res.scalars().one_or_none()
        if feedback:
            session.delete(feedback)
            await session.commit()

    async def get_all(self, user_id: int, pagination: tuple[int, int], session: AsyncSession) -> list[Base]:
        query = select(Feedback).where(Feedback.user_id == user_id).limit(pagination[1]).offset(pagination[0])
        res = await session.execute(query)
        return res.scalars().all()

feedback_crud = FeedbacksCrud()
