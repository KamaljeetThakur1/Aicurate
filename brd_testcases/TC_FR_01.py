from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def sso_login(url, username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))
            ).click()
            print("Clicked 'Login with SSO'")
        except:
            print("No 'Login with SSO' button, continuing to Microsoft login...")
        time.sleep(5)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys(username)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(5)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys(password)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(5)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='No']"))
        ).click()
        print("Declined 'Stay signed in' prompt.")
        print("Login successful.")
        return driver

    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()
        return None

