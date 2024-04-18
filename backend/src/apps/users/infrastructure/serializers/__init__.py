"""
This module is responsible for importing all the serializers that are used in the
users app.
"""

from .shelter import RegisterShelterSerializer
from .authentication import (
    AuthenticationSerializer,
    CustomTokenObtainPairSerializer,
)
from .admin import RegisterAdminSerializer
from .pet import PetReadOnlySerializer, PetSerializer
