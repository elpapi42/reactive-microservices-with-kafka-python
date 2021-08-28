import asyncio
from itertools import chain
from dataclasses import dataclass, asdict
from typing import Callable, Dict, List

from aiokafka import AIOKafkaConsumer

from source.infrastructure.loggers import default as logger


@dataclass
class KafkaSubscriber():
    """
    Allows to consume messages and
    pass them in batches to a callback.

    The continous consume of messages
    is managed by a backgroud task that
    executes on the default event loop.

    The callback must be a coroutine.
    The callback must accept a list of dicts,
    each dict representing a message.
    """
    consumer:AIOKafkaConsumer
    callback:Callable[[List[Dict]], None]

    def __post_init__(self):
        self.stopped = False
        self.task = None

    async def start(self):
        await self.consumer.start()

    async def stop(self):
        self.stopped = True

        if self.task:
            await self.task

        await self.consumer.stop()

    async def consume(self):
        while not self.stopped:
            batch = await self.consumer.getmany(
                timeout_ms=100,
                max_records=100
            )

            # Concat the messages coming from each topic-partition.
            batch = list(chain(*[b for _, b in batch.items()]))

            # ConsumerRecord to dict.
            batch = [asdict(m) for m in batch]

            if len(batch) == 0:
                # This sleep reduces overhead
                # when no messages are received.
                await asyncio.sleep(1)

                # Skip iteration
                continue

            await self.callback(batch)

            await self.consumer.commit()

            logger.info(f'Kafka: {len(batch)} messages commited')

    def subscribe(self):
        self.task = asyncio.create_task(self.consume())
