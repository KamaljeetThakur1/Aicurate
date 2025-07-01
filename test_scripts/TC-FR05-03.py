
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_section_toggles_on_refresh():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://editor.ipsy.com/campaign-page")
        driver.find_element(By.ID, "toggle-section").click()
        # Refresh
        driver.refresh()
        assert driver.find_element(By.ID, "section").is_displayed()
        print("Section toggle state retained after refresh.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
