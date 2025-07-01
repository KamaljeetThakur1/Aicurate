
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_styling_mismatch_alert():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://editor.ipsy.com/campaign-page")
        driver.find_element(By.ID, "change-style").click()
        assert "Style does not match the existing template" in driver.page_source
        print("Error message displayed correctly for styling mismatch.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
