from apps.users.domain.abstractions import IUserRepository, IPetRepository
from typing import Dict, Any


class UserRegister:
    """
    Use case that is responsible for user registration.

    This class interacts with an instance of a class implementing the `IUserRepository`
    interface, which is injected at the point of use.
    """

    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    def shelter_registration(self, data: Dict[str, Any]) -> None:
        """
        Handles the registration process for shelter users.

        Parameters:
            - data: A dictionary containing the registration data.
        """

        del data["confirm_password"]
        self._user_repository.create_shelter(data=data)

    def admin_registration(self, data: Dict[str, Any]) -> None:
        """
        Handles the registration process for admin users.

        Parameters:
            - data: A dictionary containing the registration data.
        """

        del data["confirm_password"]
        self._user_repository.create_admin(data=data)


class PetRegister:
    """
    A class used to manage the registration process of pets in the system.

    This class interacts with an instance of a class implementing the `IPetRepository`
    interface, which is injected at the point of use.
    """

    def __init__(self, pet_repository: IPetRepository):
        self._pet_repository = pet_repository

    def pet_registration(self, data: Dict[str, Any]) -> None:
        """
        Handles the registration process for pets.

        Parameters:
            - data: A dictionary containing the registration data.
        """

        self._pet_repository.create(data=data)
