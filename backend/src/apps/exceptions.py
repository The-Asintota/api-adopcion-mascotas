from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status
from typing import Any, Dict, Optional, Union


def services_exception_handler(
    exc: APIException, context: Dict[str, Any]
) -> Response:
    """
    Custom exception handler that handles `TokenPermissionDenied` exception.

    #### Parameters:
    - exc: The exception instance to be handled.
    - context: A dictionary containing the request object.
    """

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    if not isinstance(exc, APIException):
        raise exc
    response = exception_handler(exc, context)
    response.status_code = exc.status_code
    try:
        response.data["code"] = exc.detail["code"]
        response.data["detail"] = exc.detail["detail"]
    except TypeError:
        response.data["code"] = getattr(exc, "code", exc.default_code)
        response.data["detail"] = getattr(exc, "detail", exc.default_detail)
    return response


class DetailDictMixin:
    """
    A mixin class that provides a method to build a detailed dictionary for the error.
    """

    default_detail: str
    default_code: str

    def __init__(
        self,
        detail: Union[Dict[str, Any], str, None] = None,
        code: Optional[str] = None,
    ) -> None:
        """
        Builds a detail dictionary for the error to give more information to API
        users.
        """

        detail_dict = {
            "detail": self.default_detail,
            "code": self.default_code,
        }
        if isinstance(detail, dict):
            detail_dict.update(detail)
        elif detail is not None:
            detail_dict["detail"] = detail
        if code is not None:
            detail_dict["code"] = code
        super().__init__(detail_dict)  # type: ignore


class DatabaseConnectionError(DetailDictMixin, APIException):
    """
    Exception raised when a connection to the database cannot be established.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Unable to establish a connection with the database. Please try again later."
    default_code = "database_connection_error"

    def __init__(self, detail: str | Dict[str, Any] = None) -> None:
        if isinstance(detail, dict):
            self.detail = {"detail": detail or self.default_detail}
        else:
            self.detail = detail or self.default_detail
        self.code = self.default_code
        super().__init__(detail=self.detail, code=self.code)


class ResourceNotFoundError(DetailDictMixin, APIException):
    """
    Exception raised when a requested resource is not found.
    """

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "requested resource not found."
    default_code = "resource_not_found"

    def __init__(
        self, detail: str | Dict[str, Any] = None, code: str = None
    ) -> None:
        if isinstance(detail, dict):
            self.detail = {"detail": detail or self.default_detail}
        else:
            self.detail = detail or self.default_detail
        self.code = code or self.default_code
        super().__init__(detail=self.detail, code=self.code)


class JWTNotFoundError(DetailDictMixin, APIException):
    """
    Exception raised when a token is not found.
    """

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Token not found."
    default_code = "token_not_found"

    def __init__(self, detail: str | Dict[str, Any] = None, code: str = None):
        if isinstance(detail, dict):
            self.detail = {"detail": detail or self.default_detail}
        else:
            self.detail = detail or self.default_detail
        self.code = code or self.default_code
        super().__init__(detail=self.detail, code=self.code)
