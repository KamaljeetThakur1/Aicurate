
def unsuccessful_sso_login():
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   try:
       driver.get("https://your-application-url.com/login")
       driver.find_element(By.XPATH, "//button[contains(text(), 'Login with SSO')]").click()
       time.sleep(2)
       driver.find_element(By.ID, "i0116").send_keys("invaliduser")
       driver.find_element(By.ID, "idSIButton9").click()
       time.sleep(2)
       driver.find_element(By.ID, "i0118").send_keys("invalidpassword")
       driver.find_element(By.ID, "idSIButton9").click()
       time.sleep(2)
       assert "Invalid" in driver.page_source
   finally:
       driver.quit()
