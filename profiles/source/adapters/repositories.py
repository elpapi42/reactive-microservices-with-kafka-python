from uuid import UUID
from typing import Dict, Optional
from dataclasses import dataclass, field

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from source.domain.entities import Profile
from source.ports.repositories import ProfileRepository
from source.infrastructure.tables import ProfileModel
from source.infrastructure.loggers import default as logger


@dataclass
class FakeProfileRepository(ProfileRepository):

    registry:Dict[UUID, Profile] = field(default_factory=dict)

    async def add(self, profile:Profile):
        self.registry[profile.user_id] = profile

    async def get_by_user_id(self, user_id:UUID) -> Optional[Profile]:
        return self.registry.get(user_id)

fake_profile_repository = FakeProfileRepository()

@dataclass
class PostgresProfileRepository(ProfileRepository):
    session:AsyncSession

    def __post_init__(self):
        # TODO: This local registry is hack, for upserts
        # sqlalchemy requires keep track of extracted
        # records from db, that is difficult with repo
        # pattern, so we need to keep track of them here,
        # there must be a better way
        self.registry:Dict[UUID, ProfileModel] = {}

    async def add(self, profile:Profile):
        profile_model = self.registry.get(profile.user_id)

        if profile_model:
            profile_model.bio = profile.bio
            profile_model.age = profile.age
            profile_model.gender = profile.gender
        else:
            profile_model = ProfileModel(**profile.dict())

        self.session.add(profile_model)

    async def get_by_user_id(self, user_id:UUID) -> Optional[Profile]:
        query = select(ProfileModel).where(ProfileModel.user_id == user_id)

        profile = (await self.session.exec(query)).first()

        if not profile:
            return None

        self.registry[user_id] = profile

        return Profile(
            user_id=profile.user_id,
            bio=profile.bio,
            age=profile.age,
            gender=profile.gender
        )
