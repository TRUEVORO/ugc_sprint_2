from uuid import UUID

from .mixin import UUIDMixin


class _LikesRequest(UUIDMixin):
    """Base likes request."""

    movie_id: UUID
    user_id: UUID


class LikeRequest(_LikesRequest):
    """Like request."""

    pass


class DislikeRequest(_LikesRequest):
    """Dislike request."""

    pass
