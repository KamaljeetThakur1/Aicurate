
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def filter_data_incorrect_dates(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.find_element(By.ID, "filter_section").click()
        driver.find_element(By.ID, "start_date_picker").send_keys(start_date)
        driver.find_element(By.ID, "end_date_picker").send_keys(end_date)
        # Click apply filter
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(2)
        error_message_displayed = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "error_message_id"))
        )
        assert "End date must be after start date" in error_message_displayed.text
        print("Error validation for incorrect date input displayed.")
    except Exception as e:
        print(f"Filtering failed due to: {e}")
    finally:
        driver.quit()
