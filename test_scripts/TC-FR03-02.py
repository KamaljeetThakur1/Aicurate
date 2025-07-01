
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_ab_testing_activation_failure():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://admin.ipsy.com")
        # Attempt to activate A/B testing without necessary permissions
        driver.find_element(By.ID, "ab-testing-settings").click()
        driver.find_element(By.ID, "toggle-ab-testing").click()
        assert "Access Denied" in driver.page_source
        print("Error message displayed when trying to enable A/B testing without permissions.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
