from typing import Annotated
from uuid import UUID
from http import HTTPStatus

from fastapi import APIRouter, Depends, Path

from core import security_jwt_remote
from models import ReviewRequest, ReviewResponse
from services import ReviewService, get_review_service

router = APIRouter(
    prefix='/api/v1',
    tags=['review'],
)


@router.post(
    '/<{movie_id}:UUID>/review',
    summary='Add review to movie',
    description='Add review to specific movie',
    response_model=None,
)
async def add_review(
    movie_id: Annotated[UUID, Path(title='movie id', description='parameter - movie id')],
    request: ReviewRequest,
    user_id: UUID = Depends(security_jwt_remote),
    review_service: ReviewService = Depends(get_review_service),
) -> HTTPStatus:

    await review_service.create({'movie_id': movie_id, 'user_id': user_id, **request.dict()})
    return HTTPStatus.OK


@router.get(
    '/<{movie_id}:UUID>/review',
    summary='Retrieve movie reviews',
    description='Retrieve specific movie reviews',
)
async def retrieve_reviews(
    movie_id: Annotated[UUID, Path(title='movie id', description='parameter - movie id')],
    review_service: ReviewService = Depends(get_review_service),
) -> list[ReviewResponse]:

    reviews = await review_service.retrieve_many({'movie_id': movie_id})
    return [ReviewResponse(**review) for review in reviews]


@router.delete(
    '/<{movie_id}:UUID>/review',
    summary='Delete review from movie',
    description='Delete review from specific movie',
    response_model=None,
)
async def delete_review(
    movie_id: Annotated[UUID, Path(title='movie id', description='parameter - movie id')],
    request: ReviewRequest,
    user_id: UUID = Depends(security_jwt_remote),
    review_service: ReviewService = Depends(get_review_service),
) -> HTTPStatus:

    await review_service.delete({'movie_id': movie_id, 'user_id': user_id, **request.dict()})
    return HTTPStatus.OK
