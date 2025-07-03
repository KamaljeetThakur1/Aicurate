
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def sso_login_edge():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('https://example.com/login')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))).click()
        driver.find_element(By.ID, "signIn").click()
        error_message_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "error")))
        assert 'Username required' in error_message_user.text
        driver.find_element(By.ID, "username").send_keys('testUser')
        driver.find_element(By.ID, "signIn").click()
        error_message_pass = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "error")))
        assert 'Password required' in error_message_pass.text
        print("Edge case handled correctly.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
sso_login_edge()
