# import os
# from dotenv import load_dotenv
# import requests
# import pytest
#
# load_dotenv()
#
# HOST = "Test_URL" if os.environ.get["Stage"] == "qa" else "Pros_URL"
#
# @pytest.fixture(autouse=True, scope='session')
# def init_environment():
#     response = requests.post(
#         url = f"{HOST}/setup",
#         headers = {"AUTHORIZATION": f"Bearer {os.getenv('API_TOKEN')}"}
#     )
#     assert response.status_code == 205