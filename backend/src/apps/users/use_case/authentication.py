from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from typing import Dict, Tuple
from apps.users.domain.abstractions import IJWTRepository, ITokenClass
from apps.users.domain.typing import AccessToken, RefreshToken, JWToken
from apps.users.models import BaseUser
from apps.exceptions import UserInactiveError


class Authentication:
    """
    Use case that is responsible for authenticating the user.

    This class is responsible for managing the process of authenticating the user.
    Interacts with `JWTRepository` and `TokenClass`, this dependency is injected at
    the point of use.

    Attributes:
    - jwt_repository: An instance of a class implementing the `IJWTRepository`
    interface.
    - jwt_class: A class that is used to generate access and refresh tokens.
    """

    def __init__(
        self, jwt_class: ITokenClass, jwt_repository: IJWTRepository
    ) -> None:
        self._jwt_class = jwt_class
        self._jwt_repository = jwt_repository

    def _generate_tokens(
        self, user: BaseUser
    ) -> Tuple[AccessToken, RefreshToken]:
        refresh = self._jwt_class.get_token(user=user)
        access = refresh.access_token

        return str(access), str(refresh)

    def authenticate_user(
        self, credentials: Dict[str, str]
    ) -> Dict[str, JWToken]:
        """
        Authenticate a user with the given credentials and return access and refresh
        tokens.
        """

        user = authenticate(**credentials)

        if not user:
            raise AuthenticationFailed(
                code="authentication_failed",
                detail="Correo o contraseña inválida.",
            )
        elif not user.is_active:
            raise UserInactiveError(
                detail="Cuenta del usuario inactiva.",
                code="authentication_failed",
            )

        refresh, access = self._generate_tokens(user=user)

        for token in [access, refresh]:
            self._jwt_repository.add_to_checklist(
                token=token,
                user=user,
            )

        return {"access": access, "refresh": refresh}
