
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
####
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_pro_number_filter_no_input():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('URL_OF_DATA_PAGE')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "filter_menu"))).click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Contains')]").click()
        driver.find_element(By.ID, "apply_filter").click()
        assert 'Please enter a PRO Number' in driver.page_source
        print("Proper error message displayed.")
    finally:
        driver.quit()
