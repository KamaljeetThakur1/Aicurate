
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_customer_platform():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/platform")
        time.sleep(2)
        assert "Customer Interaction" in driver.title
        assert driver.find_element(By.ID, "chat")  # Element ID for chat is assumed
        assert driver.find_element(By.ID, "feedback")  # Element ID for feedback is assumed
        print("Platform loaded successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
