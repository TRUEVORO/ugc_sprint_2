from functools import lru_cache

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from db import get_mongo
from repositories import MongoRepository


class ReviewService(MongoRepository):
    """Review service."""

    def __init__(self, mongo: AsyncIOMotorClient) -> None:
        """Initialization of review service."""

        super().__init__(mongo, 'reviews')


@lru_cache()
def get_review_service(mongo: AsyncIOMotorClient = Depends(get_mongo)) -> ReviewService:
    """Get review service."""

    return ReviewService(mongo)
