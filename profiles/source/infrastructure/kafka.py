from aiokafka import AIOKafkaConsumer

from source.infrastructure.settings import application_settings

producer = AIOKafkaConsumer()
