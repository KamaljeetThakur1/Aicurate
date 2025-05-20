from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def clear_date_filters(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'date-picker')))
        driver.find_element(By.XPATH, "//button[contains(text(), 'Clear Filters')]").click()
        time.sleep(2)
        assert "All data displayed" in driver.page_source, "Data not cleared correctly"
    finally:
        driver.quit()
