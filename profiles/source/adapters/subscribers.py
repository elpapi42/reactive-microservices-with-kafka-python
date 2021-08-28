from typing import List, Dict

from source.infrastructure.kafka.subscriber import KafkaSubscriber
from source.infrastructure.kafka.consumers import users_consumer
from source.infrastructure.loggers import default as logger


async def create_profile(messages:List[Dict]):

    messages = [m for m in messages if m['headers']['event_type'] == 'KafkaUserRegistered']

    for message in messages:
        logger.info(f'{message}')

create_profile_subscriber = KafkaSubscriber(users_consumer, create_profile)
