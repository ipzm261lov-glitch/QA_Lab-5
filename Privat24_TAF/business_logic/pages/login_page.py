
from selenium.webdriver.common.by import By
from core.wait_utils import WaitUtils
from core.logger import get_logger


class LoginPage:
    """Page Object for Privat24 login page."""

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.ID, "error-message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)
        self.logger = get_logger(self.__class__.__name__)

    def open(self, base_url):
        self.driver.get(f"{base_url}/login")
        self.logger.info("Login page opened")

    def enter_username(self, username):
        field = self.wait.wait_for_element(
            self.USERNAME_INPUT
        )
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.wait_for_element(
            self.PASSWORD_INPUT
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.wait_for_clickable(
            self.LOGIN_BUTTON
        ).click()

        self.logger.info("Login button clicked")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.wait.wait_for_element(
            self.ERROR_MESSAGE
        ).text