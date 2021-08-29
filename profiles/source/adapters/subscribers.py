import asyncio
from logging import log
from uuid import UUID
from typing import List, Dict

from source.infrastructure.loggers import default as logger
from source.infrastructure.kafka.subscriber import KafkaSubscriber
from source.infrastructure.kafka.consumers import users_consumer
from source.application.create_profile import CreateProfileService
from source.adapters.repositories import PostgresProfileRepository


async def create_profiles_batch(messages:List[Dict]):
    repo = PostgresProfileRepository()
    service = CreateProfileService(repo)

    user_ids = [
        UUID(m['value']['id'])
        for m in messages
        if m['headers'].get('event_type') == 'UserRegistered'
    ]

    await asyncio.gather(*[service.execute(user_id) for user_id in user_ids])

create_profile_subscriber = KafkaSubscriber(users_consumer, create_profiles_batch)
