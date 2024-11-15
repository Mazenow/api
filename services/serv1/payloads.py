from faker import Faker

fake = Faker()


class Payloads:
    pass
    create_user = {
            "id": 112,
            "category": {
                        "id": 1,
                        "name": "string"
                            },
            "name": fake.name(),
            "photoUrls": [
                        "string"
                            ],
            "tags": [
                    {
                      "id": 1,
                      "name": "string"
                    }
                ],
            "status": "available"
    }
