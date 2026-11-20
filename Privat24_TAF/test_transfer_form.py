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

    # 2. Очікуємо Dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )

    # 3. Перехід до форми переказу
    driver.find_element(By.ID, "transfer-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/transfer")
    )

    # 4. Знаходимо поля форми
    recipient = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "recipient"))
    )

    amount = driver.find_element(By.ID, "amount")

    submit_button = driver.find_element(By.ID, "submit-transfer")

    # 5. Вводимо тестові дані
    recipient.send_keys("TEST_RECIPIENT_001")
    amount.send_keys("500.00")

    # 6. Перевіряємо введені значення
    assert recipient.get_attribute("value") == "TEST_RECIPIENT_001"
    assert amount.get_attribute("value") == "500.00"
    assert submit_button.is_displayed()
    assert submit_button.is_enabled()

    print("Recipient:", recipient.get_attribute("value"))
    print("Amount:", amount.get_attribute("value"))
    print("Submit button is available:", submit_button.is_enabled())
    print("TEST PASSED: Transfer form works correctly!")

finally:
    driver.quit()