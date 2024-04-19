from django.core.management.base import BaseCommand
from django.db import OperationalError, utils
from apps.users.domain.constants import PET_TYPES
from apps.users.models import PetType


class Command(BaseCommand):

    help = "Add pet types to the database."

    def handle(self, *args, **kwargs) -> None:

        self.stdout.write(self.style.MIGRATE_HEADING("Added pet type:"))

        for pet_type in PET_TYPES:
            try:
                PetType.objects.create(type=pet_type)
                self.stdout.write(
                    f"  {self.style.MIGRATE_LABEL('Creating record')}: {pet_type}... "
                    + self.style.SUCCESS("OK")
                )
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Could not add pet type, database out of order."
                    )
                )
            except utils.IntegrityError:
                self.stdout.write(
                    f"  {self.style.MIGRATE_LABEL('Creating record')}: {pet_type}... "
                    + self.style.WARNING("Already exists.")
                )
