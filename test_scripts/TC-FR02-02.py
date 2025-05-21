def test_access_chat_without_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://maya.com/chat")
        assert "Login" in driver.title
    finally:
        driver.quit()