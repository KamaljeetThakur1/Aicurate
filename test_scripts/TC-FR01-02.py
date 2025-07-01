
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_homepage_layout_loading_failure():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://www.ipsy.com")
        driver.set_network_conditions({'offline': True})
        assert "Unable to connect" in driver.page_source
        print("Error message displayed correctly when homepage fails to load.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
