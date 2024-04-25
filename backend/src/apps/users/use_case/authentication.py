from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.db.models import Model
from typing import Dict, Tuple
from apps.users.domain.abstractions import IJWTRepository, ITokenClass
from apps.users.domain.typing import AccessToken, RefreshToken, JWToken
from apps.exceptions import UserInactiveError


class Authentication:
    """
    Use case that is responsible for authenticating the user.

    This class interacts with instances of classes implementing the `ITokenClass` and
    `IJWTRepository` interfaces, which are injected at the point of use.
    """

    def __init__(
        self, jwt_class: ITokenClass, jwt_repository: IJWTRepository
    ) -> None:
        self._jwt_class = jwt_class
        self._jwt_repository = jwt_repository

    def _generate_tokens(
        self, user: Model
    ) -> Tuple[AccessToken, RefreshToken]:
        """
        Generates access and refresh tokens for a given user.

        #### Parameters:
        - user: An instance of the `Shelter` or `AdminUser` model.
        """

        refresh = self._jwt_class.get_token(user=user)
        access = refresh.access_token

        return str(access), str(refresh)

    def authenticate_user(
        self, credentials: Dict[str, str]
    ) -> Dict[str, JWToken]:
        """
        Authenticates a user with the given credentials and returns access and refresh
        tokens.

        #### Parameters:
        - credentials: A dictionary containing the user's credentials.

        #### Raises:
        - AuthenticationFailed: If the authentication process fails.
        - UserInactiveError: If the user is inactive.
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

        access, refresh = self._generate_tokens(user=user)

        for token in [access, refresh]:
            self._jwt_repository.add_to_checklist(
                token=token,
                user=user,
            )

        return {
            "access": access,
            "refresh": refresh,
            "role": user.content_type.model_class().__name__,
        }
