import logging
from contextlib import asynccontextmanager

import uvicorn
from aiokafka import AIOKafkaProducer
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

from api.v1 import bookmark_router, like_router, review_router, view_router
from brokers import KafkaProducer, kafka_broker
from core import LOGGING, settings
from db import mongo


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    aio_kafka_producer: AIOKafkaProducer = AIOKafkaProducer(
        bootstrap_servers=settings.kafka_dsn.removeprefix('kafka://')
    )
    await aio_kafka_producer.start()
    kafka_broker.kafka_producer = KafkaProducer(aio_kafka_producer)

    mongo.mongo = AsyncIOMotorClient(host=settings.mongo_dsn.host, port=int(settings.mongo_dsn.port), maxPoolSize=10)

    yield

    await kafka_broker.kafka_producer.producer.stop()

    mongo.mongo.close()


app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    description='User movie progress view',
    version='1.0.0',
    lifespan=lifespan,
)

app.include_router(bookmark_router)
app.include_router(like_router)
app.include_router(review_router)
app.include_router(view_router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8001,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
