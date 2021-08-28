from typing import List, Optional
from uuid import UUID
from dataclasses import dataclass

from pydantic import BaseModel

from source.domain.entities import Profile
from source.domain.enums import Gender
from source.ports.repositories import ProfileRepository

class CreateProfilesBatchOutputDTO(BaseModel):
    id:UUID
    user_id:UUID
    bio:Optional[str]
    age:Optional[int]
    gender:Optional[Gender]

@dataclass
class CreateProfilesBatchService():
    repo:ProfileRepository

    async def execute(
        self,
        user_ids:List[UUID]
    ) -> List[CreateProfilesBatchOutputDTO]:
        profiles = [Profile(user_id=user_id) for user_id in user_ids]

        await self.repo.add_many(profiles)

        return [CreateProfilesBatchOutputDTO(
            **profile.dict()
        ) for profile in profiles]
