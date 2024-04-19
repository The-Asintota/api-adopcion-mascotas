from rest_framework.permissions import BasePermission
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from apps.users.infrastructure.utils import decode_jwt
from apps.users.domain.constants import UserRoles


class IsAuthenticatedShelter(BasePermission):
    """
    Permission class that checks if the user is authenticated and has the role of
    shelter.
    """

    def has_permission(self, request: Request, view: GenericAPIView) -> bool:

        if not bool(request.user and request.user.is_authenticated):
            self.message = "Authentication credentials were not provided."

            return False

        access = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
        payload = decode_jwt(token=access)

        if payload["role"] != UserRoles.SHELTER.value:
            self.code = "permission_denied"
            self.message = "You are not allowed to access this resource."

            return False

        # Add the decoded token to the request object
        request.decoded_token_access = {
            "payload": payload,
            "token": access,
        }

        return True
