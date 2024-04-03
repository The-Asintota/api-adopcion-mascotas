from apps.users.domain.abstractions import IUserRepository


class UserRegister:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def shelter_registration(self, data):
        self.user_repository.create_shelter(data=data)
