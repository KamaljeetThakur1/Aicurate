
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_identify_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        driver.find_element(By.NAME, "username").send_keys("user1")
        driver.find_element(By.NAME, "password").send_keys("Pass123")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Identify Needs')]").click()
        time.sleep(2)
        assert "Identify Needs" in driver.title
        print("Needs identification section is displayed successfully.")
    finally:
        driver.quit()
