from fastapi import Depends
from fastapi.security import HTTPBearer

token_auth_scheme = HTTPBearer()


class AuthMiddleware():
    def verifyAuth0(token: str = Depends(token_auth_scheme)):
        """A valid access token is required to access this route"""
        result = token.credentials
        return result
