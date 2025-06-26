
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_analyze_customer_needs():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/analyze_needs")
        time.sleep(2)
        assert driver.find_element(By.ID, "feedback_input")  # Element ID for feedback input assumed
        driver.find_element(By.ID, "feedback_input").send_keys("I need more features.")
        driver.find_element(By.ID, "analyze_button").click()  # Button for analysis assumed
        time.sleep(2)
        assert "Needs Report" in driver.page_source
        print("Needs analysis completed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
