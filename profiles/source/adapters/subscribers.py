from uuid import UUID
from typing import List, Dict

from source.infrastructure.kafka.subscriber import KafkaSubscriber
from source.infrastructure.kafka.consumers import users_consumer
from source.infrastructure.loggers import default as logger
from source.application.create_profiles_batch import CreateProfilesBatchService
from source.adapters.repositories import fake_profile_repository


async def create_profiles_batch(messages:List[Dict]):
    repo = fake_profile_repository
    service = CreateProfilesBatchService(repo)

    user_ids = [
        UUID(m['value']['id'])
        for m in messages
        if m['headers'].get('event_type') == 'UserRegistered'
    ]

    await service.execute(user_ids)

create_profile_subscriber = KafkaSubscriber(users_consumer, create_profiles_batch)
