
import requests
from core.config import Config
from core.logger import get_logger


class APIClient:
    """REST API client for Privat24 TAF."""

    def __init__(self, base_url=None):
        self.base_url = base_url or Config.BASE_URL
        self.session = requests.Session()
        self.logger = get_logger(self.__class__.__name__)

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"

        self.logger.info(f"GET request: {url}")

        response = self.session.get(
            url,
            params=params,
            timeout=10
        )

        self.logger.info(
            f"Response status: {response.status_code}"
        )

        return response

    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}{endpoint}"

        self.logger.info(f"POST request: {url}")

        response = self.session.post(
            url,
            data=data,
            json=json,
            timeout=10
        )

        self.logger.info(
            f"Response status: {response.status_code}"
        )

        return response

    def close(self):
        self.session.close()