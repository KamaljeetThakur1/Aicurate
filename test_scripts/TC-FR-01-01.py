
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_valid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://example.com/login")
    driver.find_element(By.ID, "username").send_keys("validUser")
    driver.find_element(By.ID, "password").send_keys("validPass")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)
    assert "Chat Interface" in driver.title
    driver.quit()
