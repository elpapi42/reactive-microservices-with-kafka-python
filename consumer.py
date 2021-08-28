import asyncio
from pprint import pprint
from uuid import UUID

from aiokafka import AIOKafkaConsumer

async def consume():
    consumer = AIOKafkaConsumer(
        'users',
        bootstrap_servers='localhost:9092',
        group_id="profiles-service",
        enable_auto_commit=False,
        isolation_level="read_committed"
    )
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        while True:
            await asyncio.sleep(1)
            batch = await consumer.getmany(timeout_ms=100)
            for tp, messages in batch.items():
                print([(UUID(m.key.decode()) if m.key else None, m.value) for m in messages])
            await consumer.commit()
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

asyncio.run(consume())
