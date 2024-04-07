from rest_framework_simplejwt.utils import datetime_from_epoch
from django.db.models import Q
from django.db import OperationalError

from apps.users.infrastructure.utils import decode_jwt
from apps.users.domain.abstractions import IJWTRepository
from apps.users.domain.typing import JWToken
from apps.users.models import User, JWT
from apps.exceptions import JWTNotFoundError, DatabaseConnectionError


class JWTRepository(IJWTRepository):
    """
    JwtRepository is a class that provides an abstraction of the database operations
    for the `JWT` and `JWTBlacklisted` models.
    """

    @classmethod
    def _create_query(cls, **filters) -> Q:
        query = Q()
        for field, value in filters.items():
            query &= Q(**{field: value})

        return query

    @classmethod
    def get_token(cls, **filters) -> JWT:
        """
        Retrieve a JWT from the database based on the provided filters.

        Parameters:
        - filters: Keyword arguments that define the filters to apply.
        """

        try:
            token = cls.model_token.objects.filter(
                cls._create_query(**filters)
            ).first()
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()
        if not token:
            raise JWTNotFoundError(
                code="token_not_found",
                detail=f'Token {filters.get("token", "")} not found.',
            )

        return token

    @classmethod
    def add_to_checklist(cls, token: JWToken, user: User) -> None:
        """
        Add a token to the checklist.

        Parameters:
        - token: A JWToken.
        - user: An instance of the User model.
        """

        payload = decode_jwt(token=token)
        try:
            cls.model_token.objects.create(
                jti=payload["jti"],
                token=token,
                user=user,
                expires_at=datetime_from_epoch(ts=payload["exp"]),
            )
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()

    @classmethod
    def add_to_blacklist(cls, token: JWT) -> None:
        """
        Add a token to the blacklist.

        Parameters:
        - token: An instance of the JWT model.
        """

        try:
            cls.model_blacklist.objects.create(token=token)
        except OperationalError:
            # In the future, a retry system will be implemented when the database is
            # suddenly unavailable.
            raise DatabaseConnectionError()
