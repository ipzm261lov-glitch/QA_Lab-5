
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # 1. Відкриваємо сторінку авторизації
    driver.get("http://127.0.0.1:8000/login")

    # 2. Вводимо неправильні облікові дані
    driver.find_element(By.ID, "username").send_keys("test_user_01")
    driver.find_element(By.ID, "password").send_keys("WrongPassword123")

    # 3. Натискаємо кнопку входу
    driver.find_element(By.ID, "login-button").click()

    # 4. Очікуємо появи повідомлення про помилку
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "error-message")
        )
    )

    # 5. Перевіряємо текст повідомлення
    actual_message = error_message.text.strip()

    assert actual_message == "Invalid credentials", (
        f"Unexpected error message: {actual_message}"
    )

    # 6. Перевіряємо, що авторизація не відбулася
    assert "/dashboard" not in driver.current_url

    print("Error message:", actual_message)
    print("Current URL:", driver.current_url)
    print("TEST PASSED: Invalid login rejected successfully!")

finally:
    driver.quit()