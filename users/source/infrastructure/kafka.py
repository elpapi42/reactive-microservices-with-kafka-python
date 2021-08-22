import os

from aiokafka import AIOKafkaProducer

from source.infrastructure.settings import application_settings

producer = AIOKafkaProducer(
    bootstrap_servers=application_settings.kafka_url,
    transactional_id=f'{os.getpid()}'
)

print(os.getpid())
