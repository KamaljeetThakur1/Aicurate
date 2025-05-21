def test_chat_interface_readiness_post_wait():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://maya.com/login")
        driver.find_element(By.ID, "username").send_keys("validuser")
        driver.find_element(By.ID, "password").send_keys("validpassword")
        driver.find_element(By.ID, "loginButton").click()
        time.sleep(30)
        assert driver.find_element(By.ID, "chatInterface").is_displayed()
    finally:
        driver.quit()