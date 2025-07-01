
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_duplicate_landing_page_creation():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://campaign.ipsy.com")
        driver.find_element(By.ID, "create-landing-page").click()
        driver.find_element(By.ID, "page-title").send_keys("Spring Campaign")
        driver.find_element(By.ID, "save-landing-page").click()
        driver.find_element(By.ID, "create-landing-page").click()
        driver.find_element(By.ID, "page-title").send_keys("Spring Campaign")
        driver.find_element(By.ID, "save-landing-page").click()
        assert "Landing page with this URL already exists" in driver.page_source
        print("Error message displayed correctly for duplicate landing page.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
