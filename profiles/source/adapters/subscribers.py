from typing import List, Dict

from source.infrastructure.kafka.subscriber import KafkaSubscriber
from source.infrastructure.kafka.consumers import users_consumer
from source.infrastructure.loggers import default as logger


async def create_profile(messages:List[Dict]):
    for message in messages:
        logger.info(f'Received message: {message}')

create_profile_subscriber = KafkaSubscriber(users_consumer, create_profile)
