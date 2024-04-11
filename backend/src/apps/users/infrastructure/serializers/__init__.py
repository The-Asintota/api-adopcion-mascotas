"""
This module is responsible for importing all the serializers that are used in the
users app.

It imports the following serializers:
    - RegisterShelterSerializer: Serializer used to validate and parse the data sent
    to the shelter registration endpoint.
    - RegisterPetSerializer: Serializer used to validate and parse the data sent to
    the pet registration endpoint.
    - AuthenticationSerializer: Serializer used to validate and parse the data sent to
    the authentication endpoint.
    - RegisterAdminSerializer: Serializer used to validate and parse the data sent to
    the admin registration endpoint.
"""

from .shelter import RegisterShelterSerializer
from .pets import RegisterPetSerializer
from .authentication import AuthenticationSerializer
from .admin import RegisterAdminSerializer
