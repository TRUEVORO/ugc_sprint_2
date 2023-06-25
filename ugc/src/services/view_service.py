from functools import lru_cache

from fastapi import Depends

from brokers import AsyncBaseProducer, KafkaProducer, get_kafka_producer
from core import settings
from models import ViewProgressDto


class ViewService:
    """View service."""

    def __init__(self, producer: AsyncBaseProducer):
        """Initialization of view service."""

        self.producer: AsyncBaseProducer = producer
        self.topic: str = settings.kafka_topic

    async def produce(self, data: ViewProgressDto) -> None:
        """Produce user view progress."""

        await self.producer.produce(topic=self.topic, key=f'{data.user_id}:{data.movie_id}', data=data)


@lru_cache()
def get_view_service(producer: KafkaProducer = Depends(get_kafka_producer)) -> ViewService:
    """Get view service."""

    return ViewService(producer)
