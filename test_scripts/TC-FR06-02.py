def test_invalid_policy_query_no_result():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://maya.com/login")
        driver.find_element(By.ID, "username").send_keys("validuser")
        driver.find_element(By.ID, "password").send_keys("validpassword")
        driver.find_element(By.ID, "loginButton").click()
        driver.find_element(By.ID, "chatInput").send_keys("What is the capital of France?")
        driver.find_element(By.ID, "chatSubmit").click()
        response = driver.find_element(By.ID, "chatResponse").text
        assert response == "No relevant information found."
    finally:
        driver.quit()