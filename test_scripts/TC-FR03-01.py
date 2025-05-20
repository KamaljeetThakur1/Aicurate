from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_by_pro_number(url, pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'filter-menu')))
        driver.find_element(By.XPATH, "//button[contains(text(), 'Open Filter')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='criteria']")))
        driver.find_element(By.XPATH, "//select[@id='criteria']").click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Contains')]").click()
        driver.find_element(By.XPATH, "//input[@id='pro-number']").send_keys(pro_number)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply Filter')]").click()
        time.sleep(2)
        assert "PRO123" in driver.page_source, "Data not filtered correctly"
    finally:
        driver.quit()
