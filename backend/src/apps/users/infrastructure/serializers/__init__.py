"""
This module is responsible for importing all the serializers that are used in the
users app.
"""

from .shelter import ShelterSerializer
from .authentication import (
    AuthenticationSerializer,
    CustomTokenObtainPairSerializer,
)
from .admin import AdminSerializer
from .pet import PetReadOnlySerializer, PetSerializer
