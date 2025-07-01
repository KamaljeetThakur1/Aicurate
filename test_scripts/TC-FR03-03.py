
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_multiple_ab_tests():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://admin.ipsy.com")
        # Setup multiple A/B tests
        driver.find_element(By.ID, "setup-ab-test-1").click()
        driver.find_element(By.ID, "setup-ab-test-2").click()
        driver.find_element(By.ID, "view-active-tests").click()
        assert len(driver.find_elements(By.CLASS_NAME, "active-ab-test")) == 2
        print("Multiple A/B tests are functioning correctly.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
