import json
from pathlib import Path


class DataProvider:
    """Loads external JSON test data."""

    @staticmethod
    def load_json(file_path):

        path = Path(file_path)

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def get_test_data(file_path, category):

        data = DataProvider.load_json(file_path)

        if category not in data:
            raise KeyError(
                f"Test data category not found: {category}"
            )

        return data[category]

from core.data_provider import DataProvider
from core.config import Config

users = DataProvider.get_test_data(
    Config.USERS_FILE,
    "invalid_users"
)

print(users)