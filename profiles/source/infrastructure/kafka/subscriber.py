import json
import asyncio
import traceback
from itertools import chain
from dataclasses import dataclass, asdict
from typing import Callable, Dict, List

from aiokafka import AIOKafkaConsumer

from source.infrastructure.loggers import default as logger


@dataclass
class KafkaSubscriber():
    """
    Allows to consume messages and pass them in batches to a callback.

    The continous consume of messages is managed by a
    backgroud task that executes on the default event loop.

    The callback must be a coroutine.

    The callback must accept a list of dicts, each dict representing a message.
    """
    consumer:AIOKafkaConsumer
    callback:Callable[[List[Dict]], None]

    def __post_init__(self):
        self.stopped = False
        self.task = None
        self.topics = []

    async def start(self):
        await self.consumer.start()

        self.topics = list(await self.consumer.topics())
        logger.info(f'Kafka: Subscriber to topics {self.topics} started')

    async def stop(self):
        self.stopped = True

        if self.task:
            await self.task

        await self.consumer.stop()

        logger.info(f'Kafka: Subscriber to topics {self.topics} stopped')

    async def consume(self):
        failed_messages = None

        while not self.stopped:
            # if not failed messaged pending, fetch batch
            if not failed_messages:
                batch = await self.consumer.getmany(
                    timeout_ms=100,
                    max_records=100
                )

                # Concat the messages coming from each topic-partition.
                batch = list(chain(*[b for _, b in batch.items()]))

                # ConsumerRecord to dict
                messages = [self.record_to_dict(record) for record in batch]
            else:
                messages = failed_messages

            # Reduces overhead when no
            # messages are received.
            if len(messages) == 0:
                await asyncio.sleep(1)
                continue

            # If the callback raises an exception,
            # it will be caught here and the messages
            # will be retried using failed_messages.
            try:
                await self.callback(messages)
            except Exception as e:
                logger.error(f'Kafka: Error processing batch: {e}')
                failed_messages = messages
                await asyncio.sleep(1)
                continue

            await self.consumer.commit()

            failed_messages = None

            logger.info(f'Kafka: {len(messages)} messages commited')

    def subscribe(self):
        self.task = asyncio.create_task(self.consume())
        logger.info(f'Kafka: Subscriber to topics {self.topics} subscribed with callback {self.callback.__name__}')

    def record_to_dict(self, record) -> Dict:
        output = asdict(record)

        output['headers'] = { 
            k:v.decode()
            for k, v
            in output['headers']
        }
        output['key'] = output['key'].decode()
        output['value'] = json.loads(output['value'].decode())

        return output
