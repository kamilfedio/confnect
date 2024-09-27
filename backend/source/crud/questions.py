from sqlalchemy import Sequence, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from source.schemas.base import Base
from source.models.questions import Question


async def get_by_event(event_id: int, session: AsyncSession) -> Sequence[Question]:
    """
    get questions by event
    Args:
        event_id (int): event id
        session (AsyncSession): current session

    Returns:
        Sequence[Question]: list of questions
    """
    query = select(Question).where(Question.event_id == event_id)
    res = await session.execute(query)
    return res.scalars().all()


async def create(question: Question, session: AsyncSession) -> Base:
    """
        create question in database
    Args:
        model (Base): question data object
        session (AsyncSession): async session

    Returns:
        Base: question object data
    """
    session.add(question)
    await session.commit()
    await session.refresh(question)

    return question


async def get_by_id(question_id: int, session: AsyncSession) -> Base | None:
    """
    get question by id
    Args:
        question_id (int): code id
        session (AsyncSession): current session

    Returns:
        Base | None: question or none
    """
    query = select(Question).where(Question.id == question_id)
    res = await session.execute(query)
    return res.scalars().one_or_none()


async def get_by_code(code: str, session: AsyncSession) -> Base | None:
    """
    get question object by code
    Args:
        code (str): code
        session (AsyncSession): current session

    Returns:
        Base | None: question object or none
    """
    query = select(Question).where(Question.code == code)
    res = await session.execute(query)
    return res.scalars().one_or_none()


async def delete(question_id: int, session: AsyncSession) -> None:
    """
    delete question by id
    Args:
        question_id (int): question id
        session (AsyncSession): current session
    """
    query = delete(Question).where(Question.id == question_id)
    await session.execute(query)
    await session.commit()
