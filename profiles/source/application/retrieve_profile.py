from uuid import UUID
from dataclasses import dataclass

from source.ports.repositories import ProfileRepository
from source.application.errors import NotFoundError
from source.application.dtos import ProfileOutputDTO


@dataclass
class RetrieveProfileService():
    repo:ProfileRepository

    async def execute(self, user_id:UUID) -> ProfileOutputDTO:
        profile = await self.repo.get_by_user_id(user_id)

        if not profile:
            raise NotFoundError('The profile does not exists')

        return ProfileOutputDTO(**profile.dict())
