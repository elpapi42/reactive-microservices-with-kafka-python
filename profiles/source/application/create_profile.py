from typing import List, Optional
from uuid import UUID
from dataclasses import dataclass

from pydantic import BaseModel

from source.domain.entities import Profile
from source.domain.enums import Gender
from source.ports.repositories import ProfileRepository
from source.infrastructure.loggers import default as logger

class CreateProfileOutputDTO(BaseModel):
    id:UUID
    user_id:UUID
    bio:Optional[str]
    age:Optional[int]
    gender:Optional[Gender]

@dataclass
class CreateProfileService():
    repo:ProfileRepository

    async def execute(
        self,
        user_id:UUID
    ) -> List[CreateProfileOutputDTO]:
        profile = await self.repo.get_by_user_id(user_id)

        if not profile:
            profile = Profile(user_id=user_id)

            await self.repo.add(profile)

        return CreateProfileOutputDTO(**profile.dict())
