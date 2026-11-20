
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.config import Config
from business_logic.pages.login_page import LoginPage
from business_logic.pages.dashboard_page import DashboardPage


def test_account_balance(driver, users_data):
    """TC-03: Verify account balance on Dashboard."""

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

    dashboard = DashboardPage(driver)

    actual_balance = dashboard.get_balance()
    expected_balance = "17000.00 UAH"

    assert actual_balance == expected_balance, (
        f"Expected: {expected_balance}, "
        f"Actual: {actual_balance}"
    )
