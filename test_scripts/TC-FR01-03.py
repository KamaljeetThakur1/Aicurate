
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_sso_login_stay_signed_in():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('URL_OF_LOGIN_PAGE')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))).click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username_field_id"))).send_keys('testuser')
        driver.find_element(By.ID, "password_field_id").send_keys('Pass123!')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        time.sleep(3)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='No']"))).click()
        print("Chose not to stay signed in.")
    finally:
        driver.quit()
