from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/chat')
    driver.find_element(By.ID, 'question-input').send_keys('Tell me a joke.')
    driver.find_element(By.ID, 'send-btn').click()
    assert "I cannot answer that" in driver.page_source
except Exception as e:
    print(f"Fallback message failed: {e}")
finally:
    driver.quit()