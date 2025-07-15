
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def empty_credentials_login(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))
        ).click()
        time.sleep(2)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)
        error_message_displayed = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "error_message_id")))
        )
        assert "Required field" in error_message_displayed.text
        print("Error message displayed for empty fields.")
    except Exception as e:
        print(f"Login failed due to: {e}")
    finally:
        driver.quit()
