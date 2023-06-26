from http import HTTPStatus

from fastapi import APIRouter, Depends

from models import LikeRequest, DislikeRequest
from services import LikesService, get_likes_service

router = APIRouter(
    prefix='/api/v1',
    tags=['likes'],
)


@router.post(
    '/like',
    summary='Like',
    description='Add like',
    response_model=None,
)
async def like(
    request: LikeRequest,
    likes_service: LikesService = Depends(get_likes_service),
) -> HTTPStatus:

    await likes_service.update(request.id, {'like': 1}, '$inc')
    return HTTPStatus.OK


@router.post(
    '/dislike',
    summary='Dislike',
    description='Add dislike',
    response_model=None,
)
async def dislike(
    request: DislikeRequest,
    likes_service: LikesService = Depends(get_likes_service),
) -> HTTPStatus:

    await likes_service.update(request.id, {'dislike': 1}, '$inc')
    return HTTPStatus.OK
