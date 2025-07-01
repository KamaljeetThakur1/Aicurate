
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def automated_sso_login():
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
       driver.find_element(By.XPATH, "//input[@value='No']").click()
       assert "Dashboard" in driver.title
   finally:
       driver.quit()
