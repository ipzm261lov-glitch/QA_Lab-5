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

    # 3. Натискаємо посилання переказу
    transfer_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "transfer-button"))
    )
    transfer_link.click()

    # 4. Очікуємо відкриття форми
    WebDriverWait(driver, 10).until(
        EC.url_contains("/transfer")
    )

    print("Current URL:", driver.current_url)
    print("TEST PASSED: Transfer page opened successfully!")

finally:
    driver.quit()