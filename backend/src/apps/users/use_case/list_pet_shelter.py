from django.db.models import QuerySet
from apps.users.domain.abstractions import IPetRepository
from apps.users.domain.typing import StrUUID
from apps.users.models import Pet


class FindPetsByShelter:
    """
    Use case that is responsible for retrieving pets from a specific shelter.

    This class interacts with an instance of a class implementing the `IPetRepository`
    interface, which is injected at the point of use.
    """

    def __init__(self, pet_repository: IPetRepository):
        self._pet_repository = pet_repository

    def get_pet(self, shelter: StrUUID) -> QuerySet[Pet]:
        """
        Retrieve pets from the database that belong to a specific shelter.

        #### Parameters:
        - shelter: The UUID of the shelter to retrieve pets from.
        """

        return self._pet_repository.get_pet_by_filters(shelter=shelter)
