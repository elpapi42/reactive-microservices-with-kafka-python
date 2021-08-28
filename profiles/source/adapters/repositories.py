from uuid import UUID
from typing import Dict, Optional
from dataclasses import dataclass, field

from source.domain.entities import Profile
from source.ports.repositories import ProfileRepository


@dataclass
class FakeProfileRepository(ProfileRepository):

    registry:Dict[UUID, Profile] = field(default_factory=dict)

    async def add(self, profile:Profile):
        self.registry[profile.id] = profile

    async def get_by_user_id(self, user_id:UUID) -> Optional[Profile]:
        return self.registry.get(user_id)

fake_profile_repository = FakeProfileRepository()
