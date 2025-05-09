from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
def test_customer_interaction_timeout():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/customer-interaction")
        start_btn = driver.find_element(By.ID, "startInteraction")
        start_btn.click()
        time.sleep(20)
        assert driver.find_element(By.ID, "timeoutMessage").is_displayed()
        print("Timeout message displayed successfully.")
    finally:
        driver.quit()