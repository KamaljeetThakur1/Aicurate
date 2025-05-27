
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://yourapp.com/login')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys('invaliduser@domain.com')
    driver.find_element(By.ID, "idSIButton9").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys('wrongpassword')
    driver.find_element(By.ID, "idSIButton9").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'error')))
    print("Error message displayed for invalid credentials")
except:
    print("Login process failed")
finally:
    driver.quit()