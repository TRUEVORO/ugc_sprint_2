from functools import lru_cache

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from db import get_mongo
from repositories import MongoRepository


class BookmarkService(MongoRepository):
    """Bookmark service."""

    def __init__(self, mongo: AsyncIOMotorClient) -> None:
        """Initialization of bookmark service."""

        super().__init__(mongo, 'bookmarks')


@lru_cache()
def get_bookmark_service(mongo: AsyncIOMotorClient = Depends(get_mongo)) -> BookmarkService:
    """Get bookmark service."""

    return BookmarkService(mongo)
