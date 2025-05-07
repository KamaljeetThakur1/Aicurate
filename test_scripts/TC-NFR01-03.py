from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/chat')
    time.sleep(5)  # Simulate slow loading
    assert "Loading..." in driver.page_source
except Exception as e:
    print(f"Chat loading failed on slow network: {e}")
finally:
    driver.quit()