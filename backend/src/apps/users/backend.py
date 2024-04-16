from django.contrib.auth.backends import ModelBackend
from django.db import OperationalError
from rest_framework.request import Request
from typing import Optional
from apps.users.infrastructure.db import UserRepository
from apps.users.models import BaseUser
from apps.exceptions import DatabaseConnectionError


class EmailBackend(ModelBackend):
    """
    A `custom authentication backend` that authenticates users based on their email
    and password.
    """

    def authenticate(
        self, request: Request, email: str, password: str
    ) -> Optional[BaseUser]:
        try:
            user = UserRepository.get_user(email=email)
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

        if not user:
            return None

        return (
            user
            if user.base_user.check_password(raw_password=password)
            else None
        )
