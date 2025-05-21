def test_valid_policy_query_code_of_conduct():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://maya.com/login")
        driver.find_element(By.ID, "username").send_keys("validuser")
        driver.find_element(By.ID, "password").send_keys("validpassword")
        driver.find_element(By.ID, "loginButton").click()
        driver.find_element(By.ID, "chatInput").send_keys("What is the code of conduct policy?")
        driver.find_element(By.ID, "chatSubmit").click()
        response = driver.find_element(By.ID, "chatResponse").text
        assert "code of conduct" in response
    finally:
        driver.quit()