from django.contrib.auth.backends import ModelBackend
from rest_framework.request import Request
from apps.users.infrastructure.db import UserRepository
from apps.users.models import User


class EmailBackend(ModelBackend):
    """
    A `custom authentication backend` that authenticates users based on their email
    and password.
    """

    user_repository = UserRepository

    def authenticate(
        self, request: Request, email: str, password: str
    ) -> User | None:

        user = self.user_repository.get(email=email).first()

        return user if user and user.check_password(password) else None
