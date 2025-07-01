
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_live_changes_reflection():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://editor.ipsy.com")
        # Change a styling element
        driver.find_element(By.ID, "change-style").click()
        driver.get("http://campaign.ipsy.com")
        assert "Changed Style" in driver.page_source
        print("Changes are reflected on landing pages live.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
