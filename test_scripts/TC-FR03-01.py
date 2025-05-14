from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_pro_number(pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/dataset")
        driver.find_element(By.XPATH, "//input[@id='pro-number']").send_keys(pro_number)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Filter')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='filtered-data']"))) 
        assert "Filtered data displayed" in driver.page_source
    finally:
        driver.quit()
