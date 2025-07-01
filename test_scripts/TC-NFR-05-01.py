
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_query_handling():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://example.com/chat")
    driver.find_element(By.ID, "inputBox").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[text()='Send']").click()
    time.sleep(2)
    assert "This query does not match any known company policy." in driver.page_source
    driver.quit()
