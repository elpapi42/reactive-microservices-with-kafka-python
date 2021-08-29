from source.domain.entities import Profile
from source.infrastructure.kafka.producers import producer
from source.ports.events import ProfileCreatedEvent


class KafkaProfileCreatedEvent(ProfileCreatedEvent):
    async def trigger(self, profile:Profile):
        async with producer.transaction():
            await producer.send_and_wait(
                topic='users',
                value=profile.json().encode(),
                key=str(profile.user_id).encode(),
                headers=[('event_type', 'ProfileCreated'.encode())]
            )
