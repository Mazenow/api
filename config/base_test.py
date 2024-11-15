from services.serv1.api_serv1 import UsersApi


class BaseTest:

    def setup_method(self):
        self.api_serv1 = UsersApi()


