
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def sso_login_invalid():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('https://example.com/login')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('invalidUser')
        driver.find_element(By.ID, "next").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys('wrongPass')
        driver.find_element(By.ID, "signIn").click()
        error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "error")))
        assert 'Invalid credentials' in error_message.text
        print("Error message displayed correctly.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
sso_login_invalid()
