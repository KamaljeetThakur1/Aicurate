
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_content_modularity():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://editor.ipsy.com")
        # Simulate adding a content module
        driver.find_element(By.ID, "add-module").click()
        assert driver.find_element(By.CLASS_NAME, "content-module").is_displayed()
        # Simulate removing a content module
        driver.find_element(By.CLASS_NAME, "remove-module").click()
        assert driver.find_elements(By.CLASS_NAME, "content-module") == []
        print("Content can be added and removed from the homepage.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
