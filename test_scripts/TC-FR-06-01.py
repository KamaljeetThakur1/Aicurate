
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_complete_policy_information():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://example.com/chat")
    driver.find_element(By.ID, "inputBox").send_keys("What are the business travel guidelines?")
    driver.find_element(By.XPATH, "//button[text()='Send']").click()
    time.sleep(2)
    assert "business travel guidelines" in driver.page_source
    driver.quit()
