"""
This module initializes the use cases of the users app.

It imports and exposes the UserRegister, PetRegister, and Authentication classes
from the register and authentication modules respectively. These classes handle
the registration and authentication processes for users and pets.

Classes:
    - UserRegister: Manages the registration process for different types of users.
    - PetRegister: Manages the registration process for pets.
    - Authentication: Manages the authentication process for users.
"""

from .register import UserRegister, PetRegister
from .authentication import Authentication
from .list_pet_shelter import FindPetsByShelter
