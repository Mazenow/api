import os


HOST = "https://petstore.swagger.io/v2" \
    # if os.environ.get["Stage"] == "qa" else "Pros_URL"

class Endpoints:
    create_user = f"{HOST}/pet"
    get_user_by_id = lambda self, pet_id: f"{HOST}/pet/{pet_id}"