
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
with priority given to user inputs.
import time

def sso_login_failure(url, username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys(username)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys(password)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)
        error_message_displayed = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "error_message_id")))
        )
        assert "Invalid username" in error_message_displayed.text
        print("Error message displayed for invalid username.")
    except Exception as e:
        print(f"SSError login failed due to: {e}")
    finally:
        driver.quit()

