
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.config import Config
from business_logic.pages.login_page import LoginPage


def test_successful_login(driver, users_data):
    """TC-01: Successful login with valid credentials."""

    user = users_data["valid_users"][0]

    login_page = LoginPage(driver)
    login_page.open(Config.BASE_URL)

    login_page.login(
        user["username"],
        user["password"]
    )

    WebDriverWait(
        driver,
        Config.EXPLICIT_WAIT
    ).until(
        EC.url_contains("/dashboard")
    )

    assert "/dashboard" in driver.current_url


def test_invalid_login(driver, users_data):
    """TC-02: Login rejection with invalid credentials."""

    user = users_data["invalid_users"][0]

    login_page = LoginPage(driver)
    login_page.open(Config.BASE_URL)

    login_page.login(
        user["username"],
        user["password"]
    )

    actual_message = login_page.get_error_message()

    assert actual_message == user["expected_error"]
    assert "/dashboard" not in driver.current_url
