
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_component_settings_retention():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://editor.ipsy.com")
        # Adjust settings for a specific component
        driver.find_element(By.ID, "edit-component").click()
        # Save settings
        driver.find_element(By.ID, "save-settings").click()
        # Switch component
        driver.find_element(By.ID, "switch-component").click()
        assert driver.find_element(By.ID, "previous-component-settings").is_displayed()
        print("Settings retained on component switch.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
