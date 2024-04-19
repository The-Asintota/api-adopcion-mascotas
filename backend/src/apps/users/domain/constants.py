from datetime import timedelta
from enum import Enum


ACCESS_TOKEN_LIFETIME = timedelta(minutes=120)
REFRESH_TOKEN_LIFETIME = timedelta(days=1)

PET_TYPES = ["Perro", "Gato"]
PET_SEX_TYPES = ["Macho", "Hembra"]


class UserRoles(Enum):

    SHELTER = "shelter"
    ADMIN_USER = "adminuser"
