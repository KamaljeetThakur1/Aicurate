from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_identify_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-needs")
        assert "Customer Needs" in driver.title
        customer_data_input = driver.find_element(By.NAME, "customerData")
        customer_data_input.send_keys("Need analysis for product X")
        assert customer_data_input.get_attribute('value') == "Need analysis for product X"
        print("Customer needs recorded successfully.")
    finally:
        driver.quit()