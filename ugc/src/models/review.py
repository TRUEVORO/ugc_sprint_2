from pydantic import Field

from .mixin import OrjsonMixin, ObjectIdMixin


class _Review(OrjsonMixin):
    """Base review."""

    review: str = Field(max_length=100)
    score: int = Field(ge=0, le=10)


class ReviewRequest(_Review):
    """Review request."""

    pass


class ReviewResponse(ObjectIdMixin, _Review):
    """Review response."""

    pass
