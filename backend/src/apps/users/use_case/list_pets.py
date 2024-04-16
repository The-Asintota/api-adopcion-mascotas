from django.db.models import QuerySet
from apps.users.domain.abstractions import IPetRepository
from apps.users.models import Pet


class PetList:
    """
    Use case that is responsible for returning the pet list.

    This class interacts with an instance of a class implementing the `IPetRepository`
    interface, which is injected at the point of use.
    """

    def __init__(self, pet_repository: IPetRepository):
        self._pet_repository = pet_repository

    def pets_list(self) -> QuerySet[Pet]:
        """
        Returns a list of all pets.
        """

        self._pet_repository.get_all_pets()
