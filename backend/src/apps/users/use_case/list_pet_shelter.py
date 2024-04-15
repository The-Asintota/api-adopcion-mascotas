from django.db.models import QuerySet
from apps.users.models import Pet
from apps.users.domain.abstractions import IPetRepository
from apps.users.domain.typing import StrUUID


class FindPetsByShelter:

    def __init__(self, pet_repository: IPetRepository):
        self._pet_repository = pet_repository

    def get_pet(self, shelter_uuid: StrUUID) -> QuerySet[Pet]:
        """
        Retrieve pets from the database that belong to a specific shelter.

        Parameters:
            - shelter_uuid (str): The UUID of the shelter to retrieve pets from.

        """
        return self._pet_repository.get_pet_by_filters(
            shelter_uuid=shelter_uuid
        )
