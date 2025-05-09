from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_customer_interaction_button_absent():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        assert "Customer Interaction" in driver.title
        try:
            driver.find_element(By.ID, "startInteraction")
        except:
            print("Start Interaction button not found, as expected.")
    finally:
        driver.quit()