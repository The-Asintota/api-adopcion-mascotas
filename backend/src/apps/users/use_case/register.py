from apps.users.domain.abstractions import IUserRepository
from typing import Dict, Any


class UserRegister:
    """
    Use case that is responsible for user registration.

    This class is responsible for managing the registration process of the
    different users defined in the system (shelter, admin). Interacts with
    `IUserRepository`, this dependency is injected at the point of use.

    Attributes:
    - user_repository: An instance of a class implementing the `IUserRepository`
    interface.
    """

    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    def shelter_registration(self, data: Dict[str, Any]) -> None:
        del data["confirm_password"]
        self._user_repository.create_shelter(data=data)

    def admin_registration(self, data: Dict[str, Any]) -> None:
        del data["confirm_password"]
        self._user_repository.create_admin(data=data)
