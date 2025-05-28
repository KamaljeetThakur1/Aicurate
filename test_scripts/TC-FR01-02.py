
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_no_internet_connection():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/home")
        driver.find_element(By.XPATH, "//a[contains(text(), 'Customer Interaction')]").click()
        time.sleep(2)
        assert "Error" in driver.page_source
        print("Error displayed for no internet connection.")
    finally:
        driver.quit()
