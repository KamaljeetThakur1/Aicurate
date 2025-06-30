
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_access_customer_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/home")
        assert "Home" in driver.title
        driver.find_element(By.LINK_TEXT, "Customer Interaction").click()
        time.sleep(2)
        assert "Interaction Options" in driver.page_source
    finally:
        driver.quit()
