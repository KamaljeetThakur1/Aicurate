
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_data_by_pro_number_invalid():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://application-url/data-filter")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "proFilterButton"))).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "filterCriteria"))).select_by_visible_text("Contains")
        driver.find_element(By.ID, "proNumberInput").send_keys("INVALID")
        driver.find_element(By.ID, 'applyFilters').click()
        no_results_message = driver.find_element(By.XPATH, "//div[@class='no-results']").text
        assert no_results_message == "No results found."
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
