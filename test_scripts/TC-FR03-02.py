from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_by_invalid_pro_number():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/data")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "proFilterMenu"))).click()
        driver.find_element(By.XPATH, "//option[text()='Contains']").click()
        driver.find_element(By.ID, "proNumberInput").send_keys("invalidPRO123")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "applyProFilter"))).click()
        time.sleep(2)
        no_results_message = driver.find_element(By.XPATH, "//div[@class='no-results']").is_displayed()
        assert no_results_message == True
        print("No results found for the invalid PRO Number.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
