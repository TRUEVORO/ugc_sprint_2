from .bookmark import router as bookmark_router
from .like import router as like_router
from .review import router as review_router
from .view import router as view_router

__all__ = ('bookmark_router', 'like_router', 'review_router', 'view_router')
