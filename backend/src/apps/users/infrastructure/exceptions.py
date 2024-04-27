from rest_framework.exceptions import APIException
from rest_framework import status
from apps.exceptions import DetailDictMixin
from typing import Dict, Any


class NotAuthenticated(APIException, DetailDictMixin):
    """
    Exception raised when the user is not authenticated.
    """

    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Authentication credentials were not provided."
    default_code = "authentication_failed"

    def __init__(
        self, detail: str | Dict[str, Any] = None, code: str = None
    ) -> None:
        if isinstance(detail, dict):
            self.detail = {"detail": detail or self.default_detail}
        else:
            self.detail = detail or self.default_detail
        self.code = code or self.default_code
        super().__init__(detail=self.detail, code=self.code)
