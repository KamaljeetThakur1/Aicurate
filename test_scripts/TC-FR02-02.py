
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_invalid_component_configuration():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://editor.ipsy.com")
        # Simulate adding an unsupported component
        driver.find_element(By.ID, "add-unsupported-module").click()
        assert "Unsupported component type" in driver.page_source
        print("Error message displayed for invalid component configuration.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
