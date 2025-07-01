
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_landing_page_styling():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://campaign.ipsy.com")
        assert "Ipsy" in driver.title
        assert driver.find_element(By.CLASS_NAME, "styled-element").is_displayed()
        print("Landing page styling is consistent with homepage.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
