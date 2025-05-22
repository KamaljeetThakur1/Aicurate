from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def sso_empty_fields(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))
        ).click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys('')
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys('')
        driver.find_element(By.ID, "idSIButton9").click()
        # Check that the user is prompted for valid input
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please enter your username')]"))
        )
        assert error_message.is_displayed(), "Error message for empty fields is not displayed."  
        print("Test passed for empty fields.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
