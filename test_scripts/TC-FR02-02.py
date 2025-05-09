from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_identify_customer_needs_invalid_input():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-needs")
        customer_data_input = driver.find_element(By.NAME, "customerData")
        customer_data_input.send_keys("")
        submit_btn = driver.find_element(By.ID, "submit")
        submit_btn.click()
        assert driver.find_element(By.ID, "errorMessage").is_displayed()
        print("Error message displayed for empty input.")
    finally:
        driver.quit()