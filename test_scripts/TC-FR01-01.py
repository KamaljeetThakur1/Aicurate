from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_customer_interaction():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        assert "Customer Interaction" in driver.title
        start_btn = driver.find_element(By.ID, "startInteraction")
        start_btn.click()
        assert driver.find_element(By.ID, "interactionPanel").is_displayed()
        print("Customer interaction initiated successfully.")
    finally:
        driver.quit()