from django.db.models import QuerySet
from typing import Dict, Any
from apps.users.domain.abstractions import IPetRepository
from apps.users.models import Pet


class PetUseCase:
    """
    Use case that is responsible for retrieving pets from a specific shelter.

    This class interacts with an instance of a class implementing the `IPetRepository`
    interface, which is injected at the point of use.
    """

    def __init__(self, pet_repository: IPetRepository):
        self._pet_repository = pet_repository

    def get_pet(self, all: bool = False, **filters) -> QuerySet[Pet] | Pet:
        """
        Retrieve pets from the database that belong to a specific shelter.

        #### Parameters:
        - all: A boolean flag that indicates whether to retrieve all pets.
        - filters: Keyword arguments that define the filters to apply.
        """

        return self._pet_repository.get_pet(all=all, **filters)

    def create_pet(self, data: Dict[str, Any]) -> None:
        """
        Handles the registration process for pets.

        #### Parameters:
        - data: A dictionary containing the registration data.
        """

        self._pet_repository.create(data=data)
