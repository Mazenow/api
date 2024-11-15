import os
from dotenv import load_dotenv

load_dotenv()

class Headers:

    basic = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }
    basic_for_get = {
        'accept': 'application/json'
                }