
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_service_unavailability_during_migration():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://www.ipsy.com")
        assert "Service unavailable" in driver.page_source
        print("Appropriate error message displayed during migration.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
