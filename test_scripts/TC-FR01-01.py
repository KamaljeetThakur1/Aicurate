
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_homepage_layout():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://www.ipsy.com")
        assert "Ipsy" in driver.title
        assert driver.find_element(By.ID, "header").is_displayed()
        assert driver.find_element(By.ID, "footer").is_displayed()
        print("New homepage layout is displayed correctly.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
