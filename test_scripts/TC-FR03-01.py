
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def filter_by_pro_number(url, pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.ID, "filter_menu").click()
        driver.find_element(By.ID, "filter_criteria").send_keys("Contains")
        driver.find_element(By.ID, "pro_number_input").send_keys(pro_number)
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(2)
        assert "results matching pro_number" in driver.page_source
        print("Dataset successfully filtered by PRO Number.")
    except Exception as e:
        print(f"Filtering by PRO Number failed due to: {e}")
    finally:
        driver.quit()
