from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/login')
    driver.find_element(By.ID, 'username').send_keys('validUser')
    driver.find_element(By.ID, 'password').send_keys('validPassword')
    driver.find_element(By.ID, 'login-btn').click()
    assert "Welcome" in driver.page_source
except Exception as e:
    print(f"Login failed: {e}")
finally:
    driver.quit()