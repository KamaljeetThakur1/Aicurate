def test_locked_account_error_message():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://maya.com/login")
        driver.find_element(By.ID, "username").send_keys("lockeduser")
        driver.find_element(By.ID, "password").send_keys("password")
        driver.find_element(By.ID, "loginButton").click()
        error_message = driver.find_element(By.ID, "error").text
        assert error_message == "This account is locked due to multiple failed attempts."
    finally:
        driver.quit()