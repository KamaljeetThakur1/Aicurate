from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_invalid_date_filter(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'date-picker')))
        driver.find_element(By.XPATH, "//input[@label='Start Date']").send_keys('2023-12-31')
        driver.find_element(By.XPATH, "//input[@label='End Date']").send_keys('2023-01-01')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]").click()
        time.sleep(2)
        error_msg = driver.find_element(By.XPATH, "//div[contains(text(), 'End date must be later than start date')]").is_displayed()
        assert error_msg == True, "Error message not displayed"
    finally:
        driver.quit()
