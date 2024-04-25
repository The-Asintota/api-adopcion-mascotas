from datetime import timedelta
from enum import Enum


class UserRoles(Enum):
    SHELTER = "ShelterProfile"
    ADMIN_USER = "AdminProfile"


ACCESS_TOKEN_LIFETIME = timedelta(minutes=120)
REFRESH_TOKEN_LIFETIME = timedelta(days=1)
PET_TYPES = ["Perro", "Gato"]
PET_SEX_TYPES = ["Macho", "Hembra"]
