from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def sso_login_invalid(url, username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))
            ).click()
        # Wait for username input
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys(username)
        driver.find_element(By.ID, "idSIButton9").click()
        # Wait for password input
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys(password)
        driver.find_element(By.ID, "idSIButton9").click()
        # Assert the error message
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))) 
        assert "Invalid username or password." in driver.page_source
    except Exception as e:
        print(f"Login failed: {e}")
    finally:
        driver.quit()
