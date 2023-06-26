from typing import Annotated
from uuid import UUID
from http import HTTPStatus

from fastapi import APIRouter, Depends, Path

from core import security_jwt_remote
from services import BookmarkService, get_bookmark_service

router = APIRouter(
    prefix='/api/v1',
    tags=['bookmark'],
)


@router.post(
    '/<{movie_id}:UUID>/bookmark',
    summary='Add movie to bookmarks',
    description='Add specific movie to bookmarks',
    response_model=None,
)
async def add_bookmark(
    movie_id: Annotated[UUID, Path(title='movie id', description='parameter - movie id')],
    user_id: UUID = Depends(security_jwt_remote),
    bookmark_service: BookmarkService = Depends(get_bookmark_service),
) -> HTTPStatus:

    await bookmark_service.create({'movie_id': movie_id, 'user_id': user_id})
    return HTTPStatus.OK


@router.delete(
    '/<{movie_id}:UUID>/bookmark',
    summary='Delete movie from bookmarks',
    description='Delete specific movie from bookmarks',
    response_model=None,
)
async def delete_bookmark(
    movie_id: Annotated[UUID, Path(title='movie id', description='parameter - movie id')],
    user_id: UUID = Depends(security_jwt_remote),
    bookmark_service: BookmarkService = Depends(get_bookmark_service),
) -> HTTPStatus:

    await bookmark_service.delete({'movie_id': movie_id, 'user_id': user_id})
    return HTTPStatus.OK
