
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_reset_filters():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('URL_OF_DATA_PAGE')
        driver.find_element(By.ID, "reset_filters").click()
        assert 'Default data state' in driver.page_source
        print("Filters reset successfully.")
    finally:
        driver.quit()
