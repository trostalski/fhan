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
        session: Optional[Session] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        token: Optional[str] = None,
        token_type: Optional[str] = "Bearer",
        login_url: Optional[str] = None,
    ):
        self.is_authenticated = False
        self.session = session
        self.method = method
        self.username = username or os.getenv("USERNAME", None)
        self.password = password or os.getenv("PASSWORD", None)
        self.token = token or os.getenv("TOKEN", None)
        self.token_type = token_type
        self.login_url = login_url or os.getenv("LOGIN_URL", None)

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
        self.session.get(self.url, auth=(self.username, self.password))

    def _bearer_auth(self):
        if not self.token or not self.login_url:
            raise AuthenticationException(
                "Token and URL are required for bearer authentication"
            )

        headers = {"Authorization": f"{self.token_type} {self.token}"}

        # Perform bearer authentication using the session
        self.session.get(self.url, headers=headers)

    def _cookie_auth(self):
        if not self.username or not self.password or not self.login_url:
            raise AuthenticationException(
                "Username, password, and login URL are required for cookie authentication."
            )

        # Perform login to get the cookie token using the session
        login_data = {"username": self.username, "password": self.password}
        self.session.post(self.login_url, data=login_data)
