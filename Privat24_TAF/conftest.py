
import pytest

from core.driver_factory import DriverFactory
from core.config import Config
from core.data_provider import DataProvider


@pytest.fixture
def driver(request):
    """Creates and manages browser lifecycle."""

    browser = DriverFactory.create_driver()

    yield browser

    try:
        if hasattr(request.node, "rep_call"):
            if request.node.rep_call.failed:

                Config.SCREENSHOTS_DIR.mkdir(
                    parents=True,
                    exist_ok=True
                )

                screenshot_path = (
                    Config.SCREENSHOTS_DIR
                    / f"{request.node.name}.png"
                )

                browser.save_screenshot(
                    str(screenshot_path)
                )

    finally:
        browser.quit()


@pytest.fixture
def users_data():
    """Provides user test data."""

    return DataProvider.load_json(
        Config.USERS_FILE
    )


@pytest.fixture
def transactions_data():
    """Provides transaction test data."""

    return DataProvider.load_json(
        Config.TRANSACTIONS_FILE
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Stores test execution results."""

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)