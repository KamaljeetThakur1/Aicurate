
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_ab_testing_activation():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://admin.ipsy.com")
        driver.find_element(By.ID, "ab-testing-settings").click()
        driver.find_element(By.ID, "toggle-ab-testing").click()
        assert driver.find_element(By.ID, "ab-testing-active").is_displayed()
        print("A/B testing functionality is successfully enabled.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
