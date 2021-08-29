from typing import Optional
from uuid import UUID
from dataclasses import dataclass

from source.domain.enums import Gender
from source.ports.repositories import ProfileRepository
from source.ports.events import ProfileUpdatedEvent
from source.application.errors import NotFoundError
from source.application.dtos import ProfileOutputDTO


@dataclass
class UpdateProfileService():
    repo:ProfileRepository
    profile_updated_event:ProfileUpdatedEvent

    async def execute(
        self,
        user_id:UUID,
        bio:Optional[str]=None,
        age:Optional[int]=None,
        gender:Optional[Gender]=None
    ) -> ProfileOutputDTO:
        profile = await self.repo.get_by_user_id(user_id)

        if not profile:
            raise NotFoundError('The profile does not exists')

        if bio is not None:
            profile.bio = bio
        if age is not None:
            profile.age = age
        if gender is not None:
            profile.gender = gender

        await self.repo.add(profile)

        await self.profile_updated_event.trigger(profile)

        return ProfileOutputDTO(**profile.dict())
