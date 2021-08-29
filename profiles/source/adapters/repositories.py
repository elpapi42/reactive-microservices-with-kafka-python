from uuid import UUID
from typing import Dict, Optional
from dataclasses import dataclass, field

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from source.domain.entities import Profile
from source.ports.repositories import ProfileRepository
from source.infrastructure.tables import ProfileModel
from source.infrastructure.sqlalchemy import engine
from source.infrastructure.loggers import default as logger


@dataclass
class FakeProfileRepository(ProfileRepository):

    registry:Dict[UUID, Profile] = field(default_factory=dict)

    async def add(self, profile:Profile):
        self.registry[profile.id] = profile

    async def get_by_user_id(self, user_id:UUID) -> Optional[Profile]:
        return self.registry.get(user_id)

fake_profile_repository = FakeProfileRepository()

@dataclass
class PostgresProfileRepository(ProfileRepository):

    async def add(self, profile:Profile):
        profile_model = ProfileModel(**profile.dict())

        session = AsyncSession(engine) #TODO: Inject session from outside

        session.add(profile_model)

        await session.commit()

        await session.close()

    async def get_by_user_id(self, user_id:UUID) -> Optional[Profile]:
        query = select(ProfileModel).where(ProfileModel.user_id == user_id)

        session = AsyncSession(engine) #TODO: Inject session from outside

        profile = (await session.exec(query)).first()

        await session.close()

        if not profile:
            return None
        
        return Profile(
            id=profile.id,
            user_id=profile.user_id,
            bio=profile.bio,
            age=profile.age,
            gender=profile.gender
        )
