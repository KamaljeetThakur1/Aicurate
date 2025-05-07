from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/chat')
    driver.find_element(By.ID, 'question-input').send_keys('What are the implications of GDPR compliance?')
    driver.find_element(By.ID, 'send-btn').click()
    assert "GDPR means protecting personal data and ensuring user privacy." in driver.page_source
except Exception as e:
    print(f"Jargon handling failed: {e}")
finally:
    driver.quit()