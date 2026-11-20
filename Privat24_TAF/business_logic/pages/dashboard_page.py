
from selenium.webdriver.common.by import By
from core.wait_utils import WaitUtils
from core.logger import get_logger


class DashboardPage:
    """Page Object for Privat24 dashboard."""

    BALANCE_LABEL = (By.ID, "account-balance")
    TRANSFER_BUTTON = (By.ID, "transfer-button")
    USER_PROFILE = (By.ID, "user-profile")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)
        self.logger = get_logger(self.__class__.__name__)

    def get_balance(self):
        balance = self.wait.wait_for_element(
            self.BALANCE_LABEL
        ).text

        self.logger.info(
            f"Account balance retrieved: {balance}"
        )

        return balance

    def open_transfer_page(self):
        self.wait.wait_for_clickable(
            self.TRANSFER_BUTTON
        ).click()

        self.logger.info("Transfer page opened")

    def is_dashboard_displayed(self):
        return self.wait.wait_for_element(
            self.USER_PROFILE
        ).is_displayed()