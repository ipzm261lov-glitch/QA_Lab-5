from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # 1. Відкриваємо сторінку авторизації
    driver.get("http://127.0.0.1:8000/login")

    # 2. Знаходимо поля введення
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    # 3. Вводимо тестові дані
    username.send_keys("test_user_01")
    password.send_keys("TestPass123")

    # 4. Натискаємо кнопку авторизації
    driver.find_element(By.ID, "login-button").click()

    # 5. Очікуємо переходу до Dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )

    print("Current URL:", driver.current_url)
    print("TEST PASSED: Successful login!")

finally:
    driver.quit()