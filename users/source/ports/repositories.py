import abc
from uuid import UUID
from typing import Optional

from source.domain.entities import User


class UserRepository(abc.ABC):
    @abc.abstractmethod
    async def add(self, user:User):
        raise NotImplementedError()
    
    @abc.abstractmethod
    async def get(self, id:UUID) -> Optional[User]:
        raise NotImplementedError()
