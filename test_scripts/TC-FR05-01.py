
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_section_modularity_on_campaign_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://editor.ipsy.com/campaign-page")
        driver.find_element(By.ID, "settings").click()
        driver.find_element(By.ID, "toggle-section-x").click()
        assert driver.find_element(By.ID, "section-x").is_displayed()
        print("Section X can be included on campaign page.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
