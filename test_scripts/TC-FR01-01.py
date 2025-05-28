
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_customer_interaction_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/home")
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Customer Interaction')]").click()
        time.sleep(2)
        assert "Customer Interaction" in driver.title
        print("Customer interaction platform loaded successfully.")
    finally:
        driver.quit()
