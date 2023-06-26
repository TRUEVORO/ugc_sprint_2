from functools import lru_cache

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from db import get_mongo
from repositories import MongoRepository


class LikesService(MongoRepository):
    """Like service."""

    def __init__(self, mongo: AsyncIOMotorClient) -> None:
        """Initialization of likes service."""

        super().__init__(mongo, 'likes')


@lru_cache()
def get_likes_service(mongo: AsyncIOMotorClient = Depends(get_mongo)) -> LikesService:
    """Get like service."""

    return LikesService(mongo)
