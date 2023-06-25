import logging
from typing import TypeVar

from aiokafka import AIOKafkaProducer
from pydantic import BaseModel

from .base_broker import AsyncBaseProducer

logger = logging.getLogger(__name__)

ProduceModel = TypeVar('ProduceModel', bound=BaseModel)


class KafkaProducer(AsyncBaseProducer):
    """Async kafka producer."""

    def __init__(self, producer: AIOKafkaProducer) -> None:
        """Initialization of async kafka producer."""

        self.producer: AIOKafkaProducer = producer

    async def produce(self, topic: str, key: str, data: ProduceModel):
        """Produce method."""

        await self.producer.send(
            topic=topic,
            value=data.json().encode('utf-8'),
            key=key.encode('utf-8'),
        )


kafka_producer: KafkaProducer | None = None


def get_kafka_producer():
    """Get async Kafka producer."""

    return kafka_producer
