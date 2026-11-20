from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://127.0.0.1:8000/dashboard")

    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)

    assert "login" in driver.current_url.lower()

    print("TEST PASSED: Redirect to Login successful!")

finally:
    driver.quit()
