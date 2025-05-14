from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_data(start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-filter")
        driver.find_element(By.XPATH, "//input[@id='start-date']").send_keys(start_date)
        driver.find_element(By.XPATH, "//input[@id='end-date']").send_keys(end_date)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply Filter')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='filtered-data']"))) 
        assert "Filtered data displayed" in driver.page_source
    finally:
        driver.quit()
