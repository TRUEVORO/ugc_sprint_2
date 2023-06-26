from typing import Annotated
from uuid import UUID
from http import HTTPStatus

from fastapi import APIRouter, Depends, Path

from core import security_jwt_remote
from services import LikeService, get_like_service

router = APIRouter(
    prefix='/api/v1',
    tags=['like'],
)


@router.post(
    '/<{movie_id}:UUID>/like',
    summary='Like movie',
    description='Add like to specific movie',
    response_model=None,
)
async def like(
    movie_id: Annotated[UUID, Path(title='movie id', description='parameter - movie id')],
    user_id: UUID = Depends(security_jwt_remote),
    like_service: LikeService = Depends(get_like_service),
) -> HTTPStatus:

    await like_service.update({'movie_id': movie_id, 'user_id': user_id}, {'like': 1}, '$inc')
    return HTTPStatus.OK


@router.post(
    '/<{movie_id}:UUID>/dislike',
    summary='Dislike movie',
    description='Add dislike to specific movie',
    response_model=None,
)
async def dislike(
    movie_id: Annotated[UUID, Path(title='movie id', description='parameter - movie id')],
    user_id: UUID = Depends(security_jwt_remote),
    like_service: LikeService = Depends(get_like_service),
) -> HTTPStatus:

    await like_service.update({'movie_id': movie_id, 'user_id': user_id}, {'dislike': 1}, '$inc')
    return HTTPStatus.OK
