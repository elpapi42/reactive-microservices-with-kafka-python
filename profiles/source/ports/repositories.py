import abc
from uuid import UUID
from typing import Optional

from source.domain.entities import Profile


class ProfileRepository(abc.ABC):
    @abc.abstractmethod
    async def add(self, profile:Profile):
        raise NotImplementedError()

    @abc.abstractmethod
    async def get_by_user_id(self, user_id:UUID) -> Optional[Profile]:
        raise NotImplementedError()
