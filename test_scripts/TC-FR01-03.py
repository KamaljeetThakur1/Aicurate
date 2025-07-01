
def persistent_login_choice():
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   try:
       driver.get("https://your-application-url.com/login")
       driver.find_element(By.XPATH, "//button[contains(text(), 'Login with SSO')]").click()
       time.sleep(2)
       driver.find_element(By.ID, "i0116").send_keys("testuser")
       driver.find_element(By.ID, "idSIButton9").click()
       time.sleep(2)
       driver.find_element(By.ID, "i0118").send_keys("testpassword")
       driver.find_element(By.ID, "idSIButton9").click()
       time.sleep(2)
       driver.find_element(By.XPATH, "//input[@value='Yes']").click()
       assert "Dashboard" in driver.title
   finally:
       driver.quit()
