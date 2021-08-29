from source.domain.entities import User
from source.infrastructure.kafka import producer
from source.ports.events import UserRegisteredEvent

class KafkaUserRegisteredEvent(UserRegisteredEvent):
    async def trigger(self, user:User):
        await producer.send(
            topic='users',
            value=user.json().encode(),
            key=str(user.id).encode(),
            headers=[('event_type', 'UserRegistered'.encode())]
        )
