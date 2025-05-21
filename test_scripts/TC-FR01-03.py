def test_empty_credentials():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://maya.com/login")
        driver.find_element(By.ID, "loginButton").click()
        error_message = driver.find_element(By.ID, "error").text
        assert error_message == "Fields cannot be empty."
    finally:
        driver.quit()