from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def no_results_pro_filter(url, nonexistent_pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "filter_menu"))
        ).click() # Open filter menu
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "filter_contains"))
        ).click() # Select 'Contains'
        driver.find_element(By.ID, "pro_number_input").send_keys(nonexistent_pro_number)
        driver.find_element(By.ID, "apply_filters").click()  # Apply filter
        # Check if no rows are displayed (Assuming a predefined method check_no_results)
        assert check_no_results(driver), "Results are displayed when they should not be." 
        print("No results as expected for nonexistent PRO Number.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
