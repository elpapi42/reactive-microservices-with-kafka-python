import asyncio
from logging import log
from uuid import UUID
from typing import List, Dict

from sqlmodel.ext.asyncio.session import AsyncSession

from source.infrastructure.loggers import default as logger
from source.infrastructure.kafka.subscriber import KafkaSubscriber
from source.infrastructure.kafka.consumers import users_consumer
from source.application.create_profile import CreateProfileService
from source.adapters.repositories import PostgresProfileRepository
from source.adapters.events import KafkaProfileCreatedEvent
from source.infrastructure.sqlalchemy import engine



async def create_profiles_batch(messages:List[Dict]):
    session = AsyncSession(engine)
    repo = PostgresProfileRepository(session)
    profile_created_event = KafkaProfileCreatedEvent()
    service = CreateProfileService(repo, profile_created_event)

    user_ids = [
        UUID(m['value']['id'])
        for m in messages
        if m['headers'].get('event_type') == 'UserRegistered'
    ]

    await asyncio.gather(*[service.execute(user_id) for user_id in user_ids])

    # This commits and closes the session.
    # Ideally this is responsability of the UoW,
    # but we have no UoW here so lets accept
    # this hack for now.
    await session.commit()
    await session.close()

create_profile_subscriber = KafkaSubscriber(users_consumer, create_profiles_batch)
