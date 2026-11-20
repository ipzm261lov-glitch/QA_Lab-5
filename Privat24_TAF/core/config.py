
import os
from pathlib import Path
from dotenv import load_dotenv

# Коренева директорія проєкту
BASE_DIR = Path(__file__).resolve().parent.parent

# Завантаження змінних середовища
load_dotenv(BASE_DIR / ".env")

class Config:
    """Central configuration for Privat24 TAF."""

    PROJECT_NAME = "Privat24 TAF"

    BASE_URL = os.getenv(
        "BASE_URL",
        "http://127.0.0.1:8000"
    )

    BROWSER = os.getenv("BROWSER", "chrome")

    HEADLESS = os.getenv(
        "HEADLESS", "false"
    ).lower() == "true"

    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10

    SCREENSHOTS_DIR = BASE_DIR / "screenshots"
    REPORTS_DIR = BASE_DIR / "reports"

    TEST_DATA_DIR = BASE_DIR / "test_data"

    USERS_FILE = TEST_DATA_DIR / "users.json"
    TRANSACTIONS_FILE = TEST_DATA_DIR / "transactions.json"
