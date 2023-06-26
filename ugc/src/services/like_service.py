from functools import lru_cache

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from db import get_mongo
from repositories import MongoRepository


class LikeService(MongoRepository):
    """Like service."""

    def __init__(self, mongo: AsyncIOMotorClient) -> None:
        """Initialization of like service."""

        super().__init__(mongo, 'likes')


@lru_cache()
def get_like_service(mongo: AsyncIOMotorClient = Depends(get_mongo)) -> LikeService:
    """Get like service."""

    return LikeService(mongo)
