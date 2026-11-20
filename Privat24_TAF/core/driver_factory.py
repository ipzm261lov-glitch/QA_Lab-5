
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from core.config import Config


class DriverFactory:
    """Creates and configures browser instances."""

    @staticmethod
    def create_driver():

        browser = Config.BROWSER.lower()

        if browser == "chrome":
            options = Options()

            if Config.HEADLESS:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")

            driver = webdriver.Chrome(options=options)

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        driver.implicitly_wait(Config.IMPLICIT_WAIT)

        return driver