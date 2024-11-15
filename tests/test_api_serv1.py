import allure
import pytest
from config.base_test import BaseTest

"""pytest -sv --alluredir=allure-results
   allure serve allure-results
"""

@allure.epic('Administration')
@allure.feature('UserFlow')
class TestServ1(BaseTest):

    @pytest.mark.regression
    @allure.title('create new pet')
    def test_create_user(self):
        user = self.api_serv1.create_user()
        print(self.api_serv1.get_user_by_id(user.id))