
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_exclude_nonexistent_section():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://editor.ipsy.com/campaign-page")
        driver.find_element(By.ID, "exclude-nonexistent-section").click()
        assert "Section not found" in driver.page_source
        print("Error displayed correctly when trying to exclude nonexistent section.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
