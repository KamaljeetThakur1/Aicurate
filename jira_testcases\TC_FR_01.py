from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_chat_interface(driver):
    test_result = {"requirement_number": "REQ-001", "test_case_id": "TC-001-CHAT-INTERFACE", "status": "Failed", "is_fixture": True}
    
    try:
        # Wait for the "Get started" button to be clickable
        get_started_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get started')]"))
        )
        get_started_button.click()

        # Wait for chat interface to load
        time.sleep(5)

        # Verify chat interface is ready
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Ask me anything about your data (500 characters limit)']"))
        )
        print("Chat interface loaded successfully and is ready for input.")
        test_result["status"] = "Passed"
    except Exception as e:
        print(f"Error verifying chat interface: {e}")
        test_result["status"] = "Failed"
    
    return test_result