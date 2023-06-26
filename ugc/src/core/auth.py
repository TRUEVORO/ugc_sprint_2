import http

import grpc
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .config import settings
from .grpc import user_pb2, user_pb2_grpc


class JWTBearerRemoteGrpc(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str | HTTPException:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail='Invalid authentication scheme.')
            user_id = await self.verify_jwt(credentials.credentials)
            if not user_id:
                raise HTTPException(status_code=http.HTTPStatus.FORBIDDEN, detail='Invalid token or expired token.')
            return user_id
        raise HTTPException(status_code=http.HTTPStatus.FORBIDDEN, detail='Invalid authorization code.')

    @staticmethod
    async def verify_jwt(jwt_token: str) -> str | None:
        async with grpc.aio.insecure_channel(settings.auth_grpc_dsn) as channel:
            stub = user_pb2_grpc.DetailerStub(channel)
            request = user_pb2.UserTokenRequest(token=jwt_token)
            try:
                response: user_pb2.UserResponse = await stub.DetailsByToken(request)
                if response is not None:
                    return response.id
            except grpc.RpcError as e:
                raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail=e.details())
        return None


security_jwt_remote = JWTBearerRemoteGrpc()
