from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_data_by_date(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'date-picker')))
        driver.find_element(By.XPATH, "//input[@label='Start Date']").send_keys(start_date)
        driver.find_element(By.XPATH, "//input[@label='End Date']").send_keys(end_date)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]").click()
        time.sleep(2)
        assert "Date filtered" in driver.page_source, "Data not filtered correctly"
    finally:
        driver.quit()
