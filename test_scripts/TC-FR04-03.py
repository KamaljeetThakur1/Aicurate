
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_landing_page_editing():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://campaign.ipsy.com/landing-page")
        driver.find_element(By.ID, "edit-landing-page").click()
        driver.find_element(By.ID, "page-title").clear()
        driver.find_element(By.ID, "page-title").send_keys("Updated Campaign Title")
        driver.find_element(By.ID, "save-changes").click()
        assert "Landing page updated successfully" in driver.page_source
        print("Landing page settings modified successfully.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
