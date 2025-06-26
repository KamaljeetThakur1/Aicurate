
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_platform_unavailable():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/platform")
        time.sleep(2)
        error_message = driver.find_element(By.TAG_NAME, "h1").text  # Assuming the main error message is in h1
        assert "503 Service Unavailable" in error_message
        print("Service unavailable message displayed.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
