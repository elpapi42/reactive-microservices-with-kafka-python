from uuid import UUID
from dataclasses import dataclass

from source.domain.entities import Profile
from source.ports.repositories import ProfileRepository
from source.ports.events import ProfileCreatedEvent
from source.application.dtos import ProfileOutputDTO
from source.infrastructure.loggers import default as logger


@dataclass
class CreateProfileService():
    repo:ProfileRepository
    profile_created_event:ProfileCreatedEvent

    async def execute(self, user_id:UUID) -> ProfileOutputDTO:
        profile = await self.repo.get_by_user_id(user_id)

        if not profile:
            profile = Profile(user_id=user_id)

            # TODO: No trasactional guarantees here
            # maybe Unit of Work pattern can help

            await self.repo.add(profile)

            await self.profile_created_event.trigger(profile) 

        return ProfileOutputDTO(**profile.dict())
