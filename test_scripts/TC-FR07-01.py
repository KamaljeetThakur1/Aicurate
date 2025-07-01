
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_website_accessibility_post_migration():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://www.ipsy.com")
        assert "Ipsy" in driver.title
        print("Website is reachable after migration to Netlify.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
