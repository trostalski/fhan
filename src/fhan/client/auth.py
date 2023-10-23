import os
from typing import Literal, Optional

from requests import Session
from dotenv import load_dotenv

from fhan.core.exceptions import AuthenticationException

load_dotenv()


class Auth:
    def __init__(
        self,
        method: Literal["basic", "bearer", "cookie"] = "cookie",
        base_url: Optional[str] = None,
        session: Optional[Session] = None,
    ):
        self.is_authenticated = False
        self.session = session
        self.method = method
        self.username = os.getenv("USERNAME", None)
        self.password = os.getenv("PASSWORD", None)
        self.token = os.getenv("TOKEN", None)
        self.login_url = os.getenv("LOGIN_URL", base_url)

    def authenticate(self):
        if self.method == "basic":
            self._basic_auth()
        elif self.method == "bearer":
            self._bearer_auth()
        elif self.method == "cookie":
            self._cookie_auth()
        else:
            raise Exception("Invalid authentication method")

    def _basic_auth(self):
        if not self.username or not self.password or not self.url:
            raise AuthenticationException(
                "Username, password, and URL are required for basic authentication"
            )

        # Perform basic authentication using the session
        response = self.session.get(self.url, auth=(self.username, self.password))

        if response.status_code == 200:
            self.is_authenticated = True
        else:
            self.is_authenticated = False

    def _bearer_auth(self):
        if not self.token or not self.login_url:
            raise AuthenticationException(
                "Token and URL are required for bearer authentication"
            )

        headers = {"Authorization": f"Bearer {self.token}"}

        # Perform bearer authentication using the session
        response = self.session.get(self.url, headers=headers)

        if response.status_code == 200:
            self.is_authenticated = True
        else:
            self.is_authenticated = False

    def _cookie_auth(self):
        if not self.username or not self.password or not self.login_url:
            raise AuthenticationException(
                "Username, password, and login URL are required for cookie authentication."
            )

        # Perform login to get the cookie token using the session
        login_data = {"username": self.username, "password": self.password}
        response = self.session.post(self.login_url, data=login_data)

        if response.status_code == 200:
            self.is_authenticated = True
        else:
            self.is_authenticated = False

    def __call__(self):
        if not self.is_authenticated:
            self.authenticate()
        return self.is_authenticated
