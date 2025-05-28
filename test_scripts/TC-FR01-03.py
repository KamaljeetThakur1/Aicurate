
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor
import time
def load_customer_interaction_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/home")
        driver.find_element(By.XPATH, "//a[contains(text(), 'Customer Interaction')]").click()
        time.sleep(2)
        assert "Customer Interaction" in driver.title
    finally:
        driver.quit()
def test_multiple_access():
    with ThreadPoolExecutor(max_workers=100) as executor:
        for _ in range(100):
            executor.submit(load_customer_interaction_page)
