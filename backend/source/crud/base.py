from abc import ABC, abstractmethod
from sqlalchemy import Sequence

from source.schemas.base import Base
from sqlalchemy.ext.asyncio import AsyncSession

class BaseCRUD(ABC):
    @abstractmethod
    async def get_all(self, pagination: tuple[int, int], session: AsyncSession) -> Sequence[Base]:
        """ get all models from the database

        Args:
            pagination (tuple[int, int]): skip, limit
            session (AsyncSession): session db

        Returns:
            Sequence[Base]: sequence of models
        """
        pass

    @abstractmethod
    async def get_by_id(self, id: int, session: AsyncSession) -> Base | None:
        """ get model by id from the database

        Args:
            id (int): model id
            session (AsyncSession): session db

        Returns:
            Base: model or none
        """
        pass

    @abstractmethod
    async def create(self, model: Base, session: AsyncSession) -> Base:
        """ create model in the database

        Args:
            model (Base): creating model
            session (AsyncSession): session db

        Returns:
            Base: created model
        """
        pass

    @abstractmethod
    async def update(self, model: Base, session: AsyncSession) -> Base:
        """ update model in the database

        Args:
            model (Base): model with updated fields
            session (AsyncSession): session db

        Returns:
            Base: updated base
        """
        pass

    @abstractmethod
    async def delete(self, id: int, session: AsyncSession) -> None:
        """ deleting model from the database

        Args:
            id (int): deleting model id
            session (AsyncSession): session db
        """
        pass
    