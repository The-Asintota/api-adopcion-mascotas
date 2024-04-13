from django.core.management.base import BaseCommand
from django.db import OperationalError
from apps.users.domain.constants import PET_SEX_TYPES
from apps.users.models import PetSex


class Command(BaseCommand):

    help = "Add pet sex types to the database."

    def handle(self, *args, **kwargs) -> None:

        for sex_type in PET_SEX_TYPES:
            try:
                PetSex.objects.create(sex=sex_type)
                self.stdout.write(
                    self.style.MIGRATE_LABEL("  Added pet sex type: ")
                    + f"{sex_type}... {self.style.SUCCESS('OK')}"
                )
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Could not add pet sex type, database out of order."
                    )
                )
