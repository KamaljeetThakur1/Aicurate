
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
        driver.get("http://application-url/login")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))).click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys("wronguser")
        driver.find_element(By.ID, "idSIButton9").click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys("WrongPass!")
        driver.find_element(By.ID, "idSIButton9").click()
        error_message = driver.find_element(By.XPATH, "//div[@class='error']").text
        assert error_message == "Invalid credentials"
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
