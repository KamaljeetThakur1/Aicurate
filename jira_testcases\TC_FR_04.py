from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_cloud_computing(driver):
    test_result = {"requirement_number": "REQ-004", "test_case_id": "TC-004-CLOUD-COMPUTING", "status": "Failed", "is_fixture": False}
    
    try:
        # Ensure we're on the chat page
        if "chat" in driver.current_url:
            # Find the input field and enter the prompt
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Ask me anything about your data (500 characters limit)']"))
            )
            input_field.clear()  # Clear previous input
            input_field.send_keys("What is cloud computing?")
            input_field.send_keys(Keys.RETURN)

            # Wait for the response
            time.sleep(10)

            # Check the response
            page_content = driver.page_source.lower()
            expected_fallback = "sorry"
            if expected_fallback in page_content:
                print("Negative Test Case Passed: Correct fallback response received")
                test_result["status"] = "Passed"
            else:
                print("Test Case Failed: Unexpected response received")
        else:
            print("Test Case Failed: Not on chat page")
    except Exception as e:
        print(f"Error in Cloud Computing test: {e}")
    
    return test_result