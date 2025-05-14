from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def sso_login_empty():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/sso")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("SomePassword")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message']"))) 
        assert "Username is required" in driver.page_source
    finally:
        driver.quit()
