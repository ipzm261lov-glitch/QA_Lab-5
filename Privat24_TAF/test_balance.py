from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # 1. Авторизація
    driver.get("http://127.0.0.1:8000/login")

    driver.find_element(By.ID, "username").send_keys("test_user_01")
    driver.find_element(By.ID, "password").send_keys("TestPass123")
    driver.find_element(By.ID, "login-button").click()

    # 2. Очікуємо завантаження Dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )

    # 3. Знаходимо баланс
    balance = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "account-balance")
        )
    )

    actual_balance = balance.text.strip()
    expected_balance = "17000.00 UAH"

    # 4. Перевіряємо значення
    assert actual_balance == expected_balance, (
        f"Expected: {expected_balance}, Actual: {actual_balance}"
    )

    print("Actual balance:", actual_balance)
    print("TEST PASSED: Account balance is correct!")

finally:
    driver.quit()