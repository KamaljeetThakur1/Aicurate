def test_failed_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://maya.com/login")
        driver.find_element(By.ID, "username").send_keys("invaliduser")
        driver.find_element(By.ID, "password").send_keys("invalidpassword")
        driver.find_element(By.ID, "loginButton").click()
        error_message = driver.find_element(By.ID, "error").text
        assert error_message == "Invalid username or password." 
    finally:
        driver.quit()