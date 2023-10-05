from requests.auth import AuthBase

from dotenv import load_dotenv


class Auth(AuthBase):
    def __init__(self, token_type, token_value):
        pass

    def __call__(self, r):
        pass
