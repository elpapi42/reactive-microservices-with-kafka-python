import abc

from source.domain.entities import Profile


class ProfileCreatedEvent(abc.ABC):
    @abc.abstractmethod
    async def trigger(self, profile:Profile):
        raise NotImplementedError()

class ProfileUpdatedEvent(abc.ABC):
    @abc.abstractmethod
    async def trigger(self, profile:Profile):
        raise NotImplementedError()
