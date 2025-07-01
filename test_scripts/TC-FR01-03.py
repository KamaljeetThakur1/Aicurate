
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_homepage_responsive_design():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://www.ipsy.com")
        driver.set_window_size(320, 640)
        assert driver.find_element(By.ID, "mobile-menu").is_displayed()
        driver.set_window_size(1024, 768)
        assert driver.find_element(By.ID, "desktop-menu").is_displayed()
        print("Homepage adjusts correctly to different screen sizes.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
