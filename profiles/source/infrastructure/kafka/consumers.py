from aiokafka import AIOKafkaConsumer

from source.infrastructure.settings import application_settings


users_consumer = AIOKafkaConsumer(
    'users',
    bootstrap_servers=application_settings.kafka_url,
    group_id='profiles-service',
    enable_auto_commit=False
)
