import abc

from source.domain.entities import User


class UserRegisteredEvent(abc.ABC):
    @abc.abstractmethod
    async def trigger(self, user:User):
        raise NotImplementedError()
