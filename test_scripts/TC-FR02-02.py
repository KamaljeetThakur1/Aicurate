
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_feedback():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/analyze_needs")
        time.sleep(2)
        driver.find_element(By.ID, "feedback_input").send_keys("")  # Assume feedback input field
        driver.find_element(By.ID, "analyze_button").click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, "error").text  # Assuming error message displayed in a specific element
        assert "Feedback cannot be empty" in error_message
        print("Error message displayed correctly.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
