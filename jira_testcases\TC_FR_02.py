from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_leave_policy(driver):
    test_result = {"requirement_number": "REQ-002", "test_case_id": "TC-002-LEAVE-POLICY", "status": "Failed", "is_fixture": False}
    
    try:
        # Ensure we're on the chat page
        if "chat" in driver.current_url:
            # Find the input field and enter the prompt
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Ask me anything about your data (500 characters limit)']"))
            )
            input_field.clear()  # Clear previous input
            input_field.send_keys("What is the leave policy?")
            input_field.send_keys(Keys.RETURN)

            # Wait for the response to load
            time.sleep(10)

            # Check the response
            page_content = driver.page_source.lower()
            if "leave" in page_content or "policy" in page_content:
                print("Test Case Passed: Leave policy information found in the response")
                test_result["status"] = "Passed"
            else:
                print("Test Case Failed: Leave policy information not found in the response")
        else:
            print("Test Case Failed: Redirected to unexpected page or login required.")
    except Exception as e:
        print(f"Error in Leave Policy test: {e}")
    
    return test_result