from apps.users.domain.abstractions import IUserRepository
from typing import Dict, Any


class UserUsesCases:
    """
    Use case that is responsible for user registration.

    This class interacts with an instance of a class implementing the `IUserRepository`
    interface, which is injected at the point of use.
    """

    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    def register_user(self, data: Dict[str, Any], role: str) -> None:
        """
        Handles the user registration process.

        #### Parameters:
        - data: A dictionary containing the registration data.
        - role: The role of the user being registered.
        """

        del data["confirm_password"]
        self._user_repository.create(data=data, role=role)
