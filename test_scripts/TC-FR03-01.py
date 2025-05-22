from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def pro_number_filter(url, pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "filter_menu"))
        ).click()  # Open filter menu
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "filter_contains"))
        ).click()  # Select 'Contains'
        driver.find_element(By.ID, "pro_number_input").send_keys(pro_number)
        driver.find_element(By.ID, "apply_filters").click() # Click Apply
        # Verify filtered results (Assuming a predefined method verify_filtered_result)
        assert verify_filtered_result(driver, pro_number), "Filtered results do not match PRO Number input." 
        print("Filtering by PRO Number successful.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
