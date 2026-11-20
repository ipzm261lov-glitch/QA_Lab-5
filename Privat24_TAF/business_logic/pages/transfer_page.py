
from selenium.webdriver.common.by import By
from core.wait_utils import WaitUtils
from core.logger import get_logger


class TransferPage:
    """Page Object for money transfer operations."""

    RECIPIENT_INPUT = (By.ID, "recipient")
    AMOUNT_INPUT = (By.ID, "amount")
    DESCRIPTION_INPUT = (By.ID, "description")
    SUBMIT_BUTTON = (By.ID, "submit-transfer")
    SUCCESS_MESSAGE = (By.ID, "transfer-success")
    ERROR_MESSAGE = (By.ID, "transfer-error")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)
        self.logger = get_logger(self.__class__.__name__)

    def enter_recipient(self, recipient):
        field = self.wait.wait_for_element(
            self.RECIPIENT_INPUT
        )
        field.clear()
        field.send_keys(recipient)

    def enter_amount(self, amount):
        field = self.wait.wait_for_element(
            self.AMOUNT_INPUT
        )
        field.clear()
        field.send_keys(str(amount))

    def enter_description(self, description):
        field = self.wait.wait_for_element(
            self.DESCRIPTION_INPUT
        )
        field.clear()
        field.send_keys(description)

    def submit_transfer(self):
        self.wait.wait_for_clickable(
            self.SUBMIT_BUTTON
        ).click()

        self.logger.info("Transfer submitted")

    def get_success_message(self):
        return self.wait.wait_for_element(
            self.SUCCESS_MESSAGE
        ).text

    def get_error_message(self):
        return self.wait.wait_for_element(
            self.ERROR_MESSAGE
        ).text