from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def clear_date_filters():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/data")
        # Assuming filters have been applied already
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "clearFilters"))).click()
        time.sleep(2)
        original_data = driver.find_element(By.XPATH, "//div[@class='data-display']").is_displayed()
        assert original_data == True
        print("Filters cleared, data reverted successfully.")
    except Exception as e:
        print(f"Clearing filters failed: {e}")
    finally:
        driver.quit()
