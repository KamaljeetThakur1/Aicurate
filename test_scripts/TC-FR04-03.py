def test_chat_loading_message():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://maya.com/login")
        driver.find_element(By.ID, "username").send_keys("validuser")
        driver.find_element(By.ID, "password").send_keys("validpassword")
        driver.find_element(By.ID, "loginButton").click()
        time.sleep(5)
        assert driver.find_element(By.ID, "loadingMessage").is_displayed()
    finally:
        driver.quit()