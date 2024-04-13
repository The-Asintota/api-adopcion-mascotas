from django.core.management.base import BaseCommand
from django.db import OperationalError
from apps.users.domain.constants import PET_TYPES
from apps.users.models import PetType


class Command(BaseCommand):

    help = "Add pet types to the database."

    def handle(self, *args, **kwargs) -> None:

        for pet_type in PET_TYPES:
            try:
                PetType.objects.create(type=pet_type)
                self.stdout.write(
                    self.style.MIGRATE_LABEL("  Added pet type: ")
                    + f"{pet_type}... {self.style.SUCCESS('OK')}"
                )
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Could not add pet type, database out of order."
                    )
                )
