from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/chat')
    assert driver.find_element(By.ID, 'chat-interface').is_displayed()
except Exception as e:
    print(f"Chat interface failed to load: {e}")
finally:
    driver.quit()