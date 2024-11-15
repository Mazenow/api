import allure
import requests

from utils.helper import Helper
from services.serv1.payloads import Payloads
from services.serv1.endpoints import Endpoints
from config.headers import Headers
from services.serv1.models.user_model import UserModel


class UsersApi(Helper):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    @allure.step("Create User")
    def create_user(self):
        response = requests.post(
            url = self.endpoints.create_user,
            headers = self.headers.basic,
            json = self.payloads.create_user,
        )
        assert response.status_code == 200, repr(response.json())
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Get user by ID")
    def get_user_by_id(self, pet_id):
        response = requests.get(
            url=self.endpoints.get_user_by_id(pet_id),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model
