
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_pro_number_filter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('URL_OF_DATA_PAGE')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "filter_menu"))).click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Contains')]").click()
        driver.find_element(By.ID, "pro_number_input").send_keys('12345')
        driver.find_element(By.ID, "apply_filter").click()
        assert 'Filtered results for 12345' in driver.page_source
        print("PRO Number filter applied successfully.")
    finally:
        driver.quit()
