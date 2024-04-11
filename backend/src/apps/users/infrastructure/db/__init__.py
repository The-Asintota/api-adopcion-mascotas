"""
This module initializes the import of the repositories used in the application. A
repository is a class that encapsulates logic related to database queries.

It imports the following repositories:
    - UserRepository: Handles database operations related to the User model.
    - JWTRepository: Handles database operations related to the JWT and JWTBlacklisted models.
    - PetRepository: Handles database operations related to the Pet model.
"""

from .user_repository import UserRepository
from .jwt_repository import JWTRepository
from .pet_repository import PetRepository
