from typing import Optional
from enum import Enum
from uuid import UUID

from pydantic import BaseModel
from fastapi import APIRouter
from sqlmodel.ext.asyncio.session import AsyncSession

from source.adapters.repositories import PostgresProfileRepository
from source.adapters.events import KafkaProfileUpdatedEvent
from source.application.update_profile import UpdateProfileService
from source.infrastructure.sqlalchemy import engine


router = APIRouter()

class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

class UpdateProfileSchemaIn(BaseModel):
    bio:Optional[str]
    age:Optional[int]
    gender:Optional[Gender]

class UpdateProfileSchemaOut(BaseModel):
    user_id:UUID
    bio:Optional[str]
    age:Optional[int]
    gender:Optional[Gender]

@router.patch('/profiles/{user_id}', status_code=200, response_model=UpdateProfileSchemaOut)
async def update_profile(user_id:UUID, data:UpdateProfileSchemaIn):
    session = AsyncSession(engine)
    repo = PostgresProfileRepository(session)
    user_updated_event = KafkaProfileUpdatedEvent()
    service = UpdateProfileService(repo, user_updated_event)

    updated_profile = await service.execute(user_id, **data.dict())

    # This commits and closes the session.
    # Ideally this is responsability of the UoW,
    # but we have no UoW here so lets accept
    # this hack for now.
    await session.commit()
    await session.close()

    return UpdateProfileSchemaOut(**updated_profile.dict())
