from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from source.config.env_config import db_config

engine = create_async_engine(db_config.database_url, echo=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """generrated async session

    Returns:
        AsyncGenerator[AsyncSession, None]: async generator

    Yields:
        Iterator[AsyncGenerator[AsyncSession, None]]: current session
    """
    async with async_session_maker() as session:
        yield session
