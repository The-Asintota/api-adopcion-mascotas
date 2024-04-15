"""
This module is responsible for importing all the views related to the users app.

It imports the following views:
    - RegisterShelterAPIView: View used to handle the shelter registration endpoint.
    - RegisterPetAPIView: View used to handle the pet registration endpoint.
    - AuthenticationAPIView: View used to handle the authentication endpoint.
    - RegisterAdminAPIView: View used to handle the admin registration endpoint.
"""

from .register_shelter import RegisterShelterAPIView
from .authentication import AuthenticationAPIView
from .register_admin import RegisterAdminAPIView
from .register_pet import RegisterPetAPIView
from .list_pets_shelter import PetListByShelterApiView
