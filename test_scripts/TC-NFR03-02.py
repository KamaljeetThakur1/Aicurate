from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/chat')
    driver.find_element(By.ID, 'question-input').send_keys('Can you provide a detailed enumeration of the policies regarding service interruptions during periods of inclement weather?')
    driver.find_element(By.ID, 'send-btn').click()
    assert "We outline the following steps during service interruptions..." in driver.page_source
except Exception as e:
    print(f"Formatting check failed: {e}")
finally:
    driver.quit()