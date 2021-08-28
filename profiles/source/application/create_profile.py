from typing import Optional
from uuid import UUID
from dataclasses import dataclass

from pydantic import BaseModel

from source.domain.entities import Profile
from source.domain.enums import Gender
from source.ports.repositories import ProfileRepository


class CreateProfileServiceOutputDTO(BaseModel):
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
        user_id:UUID,
        bio:Optional[str]=None,
        age:Optional[int]=None,
        gender:Optional[Gender]=None,
    ) -> Profile:
        profile = Profile(
            user_id=user_id,
            bio=bio,
            age=age,
            gender=gender
        )

        await self.repo.add(profile)

        return CreateProfileServiceOutputDTO(**profile.dict())
