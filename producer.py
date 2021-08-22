import asyncio
from uuid import uuid4

from aiokafka import AIOKafkaProducer

async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        transactional_id="transactional-other"
    )
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        async with producer.transaction():
            await producer.send_and_wait("other-topic", b"Super message")#, key=uuid4().bytes
            #raise TypeError("This is a test")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

asyncio.run(send_one())
