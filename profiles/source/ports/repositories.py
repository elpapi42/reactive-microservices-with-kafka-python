import abc
from uuid import UUID
from typing import Optional, List

from source.domain.entities import Profile


class ProfileRepository(abc.ABC):
    @abc.abstractmethod
    async def add_many(self, profiles:List[Profile]):
        raise NotImplementedError()

    @abc.abstractmethod
    async def get_by_user_id(self, user_id:UUID) -> Optional[Profile]:
        raise NotImplementedError()
